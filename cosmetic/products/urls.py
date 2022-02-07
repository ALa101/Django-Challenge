from django.urls import path
from . import views


urlpatterns = [
    path('all_products',views.products, name='products'),
    path('products_detilis/<str:products_name>', views.products_detilis, name ='products_detilis'),
    path('products_detilis2/<str:products_name>', views.products_detilis2, name ='products_detilis2'), 
    path('edit_product/<str:products_name>', views.edit_product, name ='edit_product'),
    path('delete/<str:products_name>', views.delete, name ='delete_product'),
    path('add_product', views.add_product, name ='add_product'),
    # path('Dashbord', views.Dashbord, name ='Dashbord2'),
    
   
]