from django.urls import path
from . import views


urlpatterns = [
    path('all_products',views.products, name='products'),
    path('<str:products_name>', views.products_detilis, name ='products_detilis')
]