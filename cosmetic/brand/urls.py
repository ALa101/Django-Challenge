from django.urls import path
from . import views


urlpatterns = [
    path('all_brands',views.brands, name='brands'),
    path("<str:brand_name>",views.brand_detilis,name='brand_detilis' ),

]