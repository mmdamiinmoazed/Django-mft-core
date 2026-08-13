from django.urls import path
from . import views
urlpatterns = [
    path('' , views.ProductView.as_view() , name="products-page") , 
    path('<str:category>' , views.ProductView.as_view() , name="products-page") , 
    path("detail/<slug:slug>" , views.ProductDetailView.as_view() , name="product-detail-page"),
]
