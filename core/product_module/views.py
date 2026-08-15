from django.shortcuts import render
from django.views.generic import View
from . import models
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
# Create your views here.
class ProductView(View) : 
    def get(self , request , category=None) : 
        
        products = models.Product.objects.all()
        count_products = products.count()
        
        
        page_number = request.GET.get("page")


        

        # Get filters from url 
        # is_smartphone = request.GET.get("smartphone")
        # is_desktops = request.GET.get("desktops")
        # is_smartwatch = request.GET.get("smart-watch")
        # is_cameras = request.GET.get("cameras")
        # is_headphones = request.GET.get("headphones")
        # is_gaming = request.GET.get("gaming")
        # is_accessories = request.GET.get("accessories")


        # Second phase 
        the_categories = {
            "smartphone" : "smartphone" ,
            "desktops" : "desktops" , 
            "cameras" : "cameras" , 
            "smartwatch" : "smartwatch" , 
            "headphone" : "headphone", 
            "gaming" : "gaming" , 
            "accessories" : "accessories"
        }

        the_ticked_list = []
        print("Categories at first : {}".format(the_categories))
        for key,value in the_categories.items(): 
            get_filter = request.GET.get(key)
            if get_filter == "on" : 
                the_ticked_list.append(value)
                # products = models.Product.objects.filter(category__title__in = value)




        print(the_ticked_list)
        products = models.Product.objects.filter(category__title__in = the_ticked_list)
        if not products : 
            products = models.Product.objects.all()

        in_stock = request.GET.get("in-stock")
        not_in_stock = request.GET.get("not-in-stock")
        if not_in_stock == "on" : 
            products = products.filter(
                is_active = False
            )
        '''This is the end of second phase filtering 
        And this part will be completed in next days 
        There is some bugs with that they should all be fixed '''


        '''Pagination system coding starts here'''
        pg = Paginator(products , 5)
        try : 
            products = pg.page(page_number)

        except PageNotAnInteger : 
            products = pg.page(1)

        except EmptyPage : 
            products = pg.page(pg.num_pages)
        '''Pagination coding ends here '''
        # if category : 
        #     products = products.filter( category__title = category )    
        
        #     if not products : 

        #         return render(request , "product_module/product.html" , context={
        #                 "products" : products
        #             })
        return render(request , "product_module/product.html" , context={
            "products" : products , "pages" : pg , "count_products" : count_products
        })
    

class ProductDetailView(View) : 
    def get(self , request , slug) : 
        product = models.Product.objects.get(slug=slug)
        return render(request , "product_module/product_detail.html" , context={
            "product" : product
})

