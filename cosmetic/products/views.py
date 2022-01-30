from django.shortcuts import render
from.models import Products

# Create your views here.
def products(request ):
    products_set = Products.objects.all()
    context = {"products_set":products_set}

    
    return render(request,'products/all_products.html', context)

def products_detilis(request, products_name ):
    products_item = Products.objects.get(Name=products_name)
 
    context = {"products_set":products_item}

    return render(request,'products/products_deitils.html', context)
