from django.shortcuts import render ,  redirect
from django.views.generic import View
from .forms import ContactForm
from .models import ContactModel
from django.contrib.messages import success
# Create your views here.

class ContactView (View): 
    def get(self , request) : 
        form = ContactForm(request.POST or None)
        return render(request , template_name="contact/contact.html" , context={
            "form" : form
        })

def get_contact(request) : 

        form = ContactForm(request.POST or None)
        if form.is_valid() : 
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            subject = form.cleaned_data.get("subject")
            message = form.cleaned_data.get("message")
            phone = form.cleaned_data.get("phone")
            contact = ContactModel()
            contact.fullname = f"{first_name} {last_name}"
            contact.email = email 
            contact.subject = subject
            contact.message = message
            contact.phone = phone
            contact.save()
            success( request , "The message sent")
            return redirect("home-page")
        else : 
            form = ContactForm(request.POST or None)
            print("Error")
            return render(request , template_name="contact/contact.html" , context={
                "form" : form
            })