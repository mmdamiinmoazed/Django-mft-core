from django.db import models
from django.utils.text import slugify
from django.utils import timezone
import datetime
# Create your models here.

class Brand(models.Model): 
    title = models.CharField(max_length=45)
    slug = models.SlugField()
    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs) : 
        self.slug = slugify(self.title)
        
        return super().save(*args , **kwargs)
class Product (models.Model): 
    title = models.CharField(verbose_name="Title of product" , max_length=100 , null=False)
    price = models.IntegerField(verbose_name="Price of product " , null=False ) 
    quantity = models.IntegerField(verbose_name="Quantity" , null=False)
    description = models.TextField(verbose_name="Description for product" , null=False)
    rate = models.IntegerField( verbose_name="Rate from 0 to 5 " , null=False )

    image = models.ImageField(upload_to="products/" , null=True)

    slug = models.SlugField()

    category = models.ManyToManyField('Category')

    created_at = models.DateTimeField( auto_now_add=True ,  null=True )
    
    is_active = models.BooleanField(verbose_name="Active (if quantity not zero)" ,   )
    
    def __str__(self):
        return self.title
    
    def set_active(self) : 
        if self.quantity == 0 : 
            self.is_active = False
        else : 
            self.is_active = True
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        self.set_active()

        # if self.quantity == 0 : 
        #     self.is_active = False

        '''This code means 
            There is a direct connection between is_active and quantity columns'''
        
        return super().save(*args, **kwargs)

class Category(models.Model) : 
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)

    class Meta : 
        ordering = ['-created_at']
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        return super().save(*args, **kwargs)