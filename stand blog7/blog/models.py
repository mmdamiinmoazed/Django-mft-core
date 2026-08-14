from django.db import models
from django.contrib.auth import get_user_model

user=get_user_model()

class Post(models.Model):

    Adult="adult"
    Teen="teen"
    Child="child"

    AGE_FIELDS=(
        (Adult,"adult"),
        (Teen,"teen"),
        (Child,"child"),
    )

    title=models.CharField(max_length=255)
    content=models.TextField()
    active=models.BooleanField(default=False)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to="blog/",null=True,default="blog/default.jpg")
    author=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    age = models.CharField(max_length=255,default=Adult,choices=AGE_FIELDS)
    category=models.ManyToManyField('Category')


    def __str__(self):
        return self.title

    class  Meta:
        ordering=['-created_time']
        verbose_name = 'پست'
        verbose_name_plural = 'پستها'


class Category(models.Model):
    name= models.CharField(max_length=255)
    creted_time= models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


