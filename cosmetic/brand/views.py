from multiprocessing import context
from tokenize import Name
from django.shortcuts import redirect, render
from django.views import View
from .models import Brand
from .forms_brand import add_brand_form

# Create your views here.
def brands(request ):
    brand_set = Brand.objects.all()
    context = {"brand_set":brand_set}
    
    return render(request,'brand/all_brand.html', context)

def brand_detilis(request, brand_name ):
    brand_item = Brand.objects.get(Name=brand_name)
  
    context = {"brand_set":brand_item}

    return render(request,'brand/brand_deitils.html', context)

def add_brand(request):
    new_brand = add_brand_form()
    if request.method=='POST':
        new_brand = add_brand_form(request.POST)
        if new_brand.is_valid():
            new_brand.save()
            return redirect('all_brand')
    context = {'form_brand': new_brand}
    return render(request,'brand/add_brand.html',context )

def edit_brand(request,brand_name):
    get_brand = Brand.objects.get(Name = brand_name)
    new_brand = add_brand_form(instance=get_brand)
    if request.method=='POST':
        new_brand = add_brand_form(request.POST, instance=get_brand)
        if new_brand.is_valid():
            new_brand.save()
            return redirect('all_brand')
    

    context = {'form_brand': new_brand}
    return render(request,'brand/add_brand.html',context )



