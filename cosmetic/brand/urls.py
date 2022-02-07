from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('all_brands',views.brands, name='all_brand'),
    path("brand_detilis/<str:brand_name>",views.brand_detilis,name='brand_detilis' ),
    path('add_brand', views.add_brand, name = 'add_brand'),
    path('edit_brand/<str:brand_name>', views.edit_brand, name = 'edit_brand'),

]