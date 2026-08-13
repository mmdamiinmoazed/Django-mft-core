from django.urls import path
from .views import *

urlpatterns = [
    path("" , home , name="home-page") , 
    path("about/" , about , name="about-page") , 
    path("shop/" , shop , name="shop-page"),
    path("product/" , product , name="product-page") , 
    path("cart/" , cart , name="cart-page"),
    
]