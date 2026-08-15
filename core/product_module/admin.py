from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin) : 
    prepopulated_fields = {
        "slug"  : ["title"]
    }
    list_display = ["title" , "created_at" ,"description" , "quantity","rate"  ]
    search_fields = ["title" ]
    list_filter = ["rate" , "category" , "created_at" , "is_active"]
    # ordering = ["-created_at"]

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin) : 
    list_display = ["pk" , "title" , "created_at"]
    search_fields = ["title"]
    list_display_links = ["title" ]