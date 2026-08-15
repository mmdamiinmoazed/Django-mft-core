from django.shortcuts import render
from django.views.generic import View
from product_module import models
# Create your views here.
class HomeView(View) : 
    def get(self , request) : 
        # Getting recent products 
        products = models.Product.objects.order_by('-pk')[:5]

        return render(request , "home_module/home.html" , context={
            "products" : products
        })