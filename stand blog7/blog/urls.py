from django.urls import path
from . import views

app_name='blog'
urlpatterns=[
    path('posts/',views.post_list,name='posts'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
    path('posts/author/<str:auth>/',views.post_list,name='auth'),
    path('posts/age/<str:age>/',views.post_list,name='age'),
    path('posts/category/<str:cat>/',views.post_list,name='cat'),
    path('search/',views.search,name='search'),
]