from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display=["name","subject"]
    search_fields=["name","message","subject"]


admin.site.register(Contact,ContactAdmin)


