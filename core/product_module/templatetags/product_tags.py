from django import template
from product_module import models
register = template.Library()
@register.simple_tag()
def simple() :
    return "This is a simple tag"
@register.inclusion_tag("product_module/recent_products.html")
def recent_products(count=5) : 
    products = models.Product.objects.order_by("-pk")[:count]
    return {"products" : products}



@register.inclusion_tag(filename="product_module/get_all_products.html")
def get_all_products() : 
    products = models.Product.objects.all()
    return {"products" : products}



@register.filter()
def upper_case(value:str) : 
    return value.upper()