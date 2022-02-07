# from django.contrib import admin
from unicodedata import name
from django.urls import path,include
from products import views
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path("connect us/",views.creat_connect, name='connect_us'),
    path('login/', views.loginPage, name ='login'),
    path('register/', views.registerPage, name ='register'),
    path('logout/', views.logoutUser, name ='logout'),
    path('Dashbord/', views.Dashbord, name ='Dashbord'),
    path("index/", views.index, name = 'index'),
    path('shop/', views.shop, name ='shop'),
    path('about/', views.about, name ='about'),
    path('contact/', views.contact, name ='contact'),
    path('shop_single/', views.shop_single, name ='shop_single'),
    # path('navbar/',views.navbar, name='nav-bar'),

    # path("/products/",products.views.products,name='brands' ),
    # path("products/",include("products.urls"))
    # path("/brand/<slug:type_item>",brand/views.brands,name='brands' ),

    # path('makeup_chose/',views.makeup_choes, name='makeup_chose'),
    # path('makeup/<slug:type_item>',views.type_item, name= 'type_item'),
    # path('makeup/',views.type_item, name= 'type_item'),


]
