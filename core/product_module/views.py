from django.shortcuts import render
from django.views.generic import View
from . import models
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
# Create your views here.
class ProductView(View) : 
    def get(self , request , category=None) : 
        
        products = models.Product.objects.all()
        count_products = products.count()
        pg = Paginator(products , 5)
        page_number = request.GET.get("page")

      
        try : 
            products = pg.page(page_number)

        except PageNotAnInteger : 
            products = pg.page(1)

        except EmptyPage : 
            products = pg.page(pg.num_pages)

        if category : 
            products=products.filter( category__title = category )    
        
            if not products : 

                return render(request , "product_module/product.html" , context={
                        "products" : products
                    })
        
        return render(request , "product_module/product.html" , context={
            "products" : products , "pages" : pg , "count_products" : count_products
        })
    

class ProductDetailView(View) : 
    def get(self , request , slug) : 
        product = models.Product.objects.get(slug=slug)
        return render(request , "product_module/product_detail.html" , context={
            "product" : product
})

