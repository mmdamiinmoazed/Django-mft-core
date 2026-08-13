from django.urls import path
from . import views
urlpatterns = [
    path("contact" , view=views.ContactView.as_view() , name="contact-page") , 
    path("get-contact" , views.get_contact , name="get-contact")
]
