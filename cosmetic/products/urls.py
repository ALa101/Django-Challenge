from django.urls import path
from . import views


urlpatterns = [
    path('all_products',views.products, name='products'),
    path('products_detilis/<str:products_name>', views.products_detilis, name ='products_detilis'),
    path('products_detilis2/<str:products_name>', views.products_detilis2, name ='products_detilis')
]