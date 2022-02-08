from datetime import datetime
from wsgiref.util import request_uri
from django import forms, views
from django.shortcuts import redirect, render
from django.db.models import Q
from.models import Products, Type
from brand.models import Brand
from .products_form import product_Form
from django.contrib.auth.decorators import login_required
import datetime


# Create your views here.
count =0
def products(request):
    global count
    q = request.GET.get('q') if request.GET.get('q') != None else ""

    products_set = Products.objects.filter(
             Q(type__name__icontains = q) |
             Q(Name__icontains = q)    
             ).order_by('-crate_time')
    type = Type.objects.all()
    brands = Brand.objects.all()
    count = products_set.count()
    
    context = {
                "products_set":products_set,
                
                "products_type":type,
                "count":count,
                 "brands" :brands,
                 }
    return render(request,'products/all_products.html', context)

def Dashbord(request):
    products(request)
    e = datetime.datetime.now()
    date = e.strftime("%H:%M %a, %B %d")
    products_num = count
    context = {
        "date":date,
        "products_num":products_num
        }
    return render(request,'products/Dashbord.html',context)

def products_detilis(request, products_id ):
    products_item = Products.objects.get(id=products_id)
    Related_Products = Products.objects.filter(Brand = products_item.Brand)
    context = {"products_set":products_item,"Related_Products":Related_Products}
    return render(request,'products/products_deitils.html', context)

def products_detilis2(request, products_id ):
    products_item = Products.objects.get(id=products_id)
    context = {"products_set":products_item}
    return render(request,'products/products_deitils2.html', context)

@login_required(login_url=('login'))
def add_product(request):
    form = product_Form()
    if request.method == 'POST':
        form = product_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {'form':form}
    return render(request, 'products/edit_product.html', context)

@login_required(login_url=('login'))  
def edit_product(request, products_id):
    get_product = Products.objects.get(id = products_id)
    form = product_Form(instance=get_product)

    if request.method == 'POST':
        form = product_Form(request.POST, instance=get_product)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {'form':form}
    return render(request, 'products/edit_product.html', context)
@login_required(login_url=('login'))
def delete(request,products_id):
    get_product = Products.objects.get(id = products_id)
    if request.method == 'POST':
        get_product.delete()
        return redirect('products')
    context = {'obj':get_product}
    return render(request, 'products/delete.html', context)



