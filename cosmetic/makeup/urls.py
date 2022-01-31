"""cosmetic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path,include
from products import views
import products

# import brand
from . import views
# from brand import views

urlpatterns = [
    path('',views.home, name='home'),
    # path('navbar/',views.navbar, name='nav-bar'),

    # path("/products/",products.views.products,name='brands' ),
    # path("products/",include("products.urls"))
    # path("/brand/<slug:type_item>",brand/views.brands,name='brands' ),

    # path('makeup_chose/',views.makeup_choes, name='makeup_chose'),
    # path('makeup/<slug:type_item>',views.type_item, name= 'type_item'),
    # path('makeup/',views.type_item, name= 'type_item'),


]
