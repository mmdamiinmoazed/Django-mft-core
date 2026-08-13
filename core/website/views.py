from django.shortcuts import render

# Create your views here.
def home(request) : 
    return render(request , template_name="website/index.html")

# def contact(request) : 
#     return render(request , template_name="website/contact.html")
    
def about(request) : 
    return render(request , template_name="website/about.html")


def product(request) : 
    return render(request , template_name="website/product.html")



def shop(request) : 
    return render(request , template_name="website/shop.html")

def cart(request) : 
    return render(request , template_name="website/cart.html")