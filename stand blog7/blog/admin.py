from django.contrib import admin
from .models import Post,Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=["title","active","updated_time"]
    list_filter=("active",)
    search_fields=["title","content"]
    date_hierarchy="created_time"
    list_display_links=["title","updated_time"]
    # fields=["title","content"]
    # exclude=["title"]
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    search_fields=['name']




