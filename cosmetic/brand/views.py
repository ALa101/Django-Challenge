from tokenize import Name
from django.shortcuts import render
from .models import Brand

# Create your views here.
def brands(request ):
    brand_set = Brand.objects.all()
    context = {"brand_set":brand_set}
    
    return render(request,'brand/all_brand.html', context)

def brand_detilis(request, brand_name ):
    brand_item = Brand.objects.get(Name=brand_name)
    print(">>>>>>>>>>>" + brand_name)
    
    # brand_ch = None
    # for i in brand_item:
    #     if 'Ala' == 'Ala':
    #         brand_ch = i
    
    context = {"brand_set":brand_item}

    return render(request,'brand/brand_deitils.html', context)


