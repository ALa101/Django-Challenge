
from ast import For
from email import message
from itertools import count
from multiprocessing import context
from django import forms, views
from django.shortcuts import redirect, render
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from makeup.models import connect_us
from .forms import connect_us_form
from datetime import datetime
import datetime
from products.models import Products, Type,Brand
from django.db.models import Q



# Create your views here.

def home(request ):
    q = request.GET.get('q') if request.GET.get('q') != None else ""

    products = Products.objects.filter(
             Q(type__name__icontains = q) |
             Q(Name__icontains = q) |
             Q(Brand__Name__icontains = q)
             
             
               
             ).order_by('-update_time')
    Brands = Brand.objects.all()
    context = {
        "products":products,
        "Brands" :Brands,
    }
    return render(request,'makeup/home.html',context)


     
def about(request ):
    return render(request,'pages/about.html')
def contact(request ):
    return render(request,'pages/contact.html')
def shop_single(request ):
    return render(request,'pages/shop_single.html')

def creat_connect(request):
    form = connect_us_form()
    if request.method == "POST":
        form = connect_us_form(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'makeup/connect_us.html',context)


def loginPage(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist ')

        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password not exist ')
    context = {'page': page}
    return render(request, 'makeup/login_regester.html', context)
def logoutUser(requset):
    logout(requset)
    return redirect('home')

def registerPage(request):
    page = 'register'
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
         
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'An error in registeration ')
    context = {'page': page, 'form':form}
    return render(request, 'makeup/login_regester.html', context)


def getproduct():
    for i in Type:
        q = i.name
    products_type = Products.objects.filter(
             Q(type__name__icontains = q) |
             Q(Name__icontains = q)    
             ).order_by('-update_time')
    type = Type.objects.all()



    pass

# def Dashbord(request):
#     count = products
#     e = datetime.datetime.now()
#     date = e.strftime("%H:%M %a, %B %d")
#     products_num = count
#     context = {
#         "date":date,
#         "products_num":products_num
#         }
#     return render(request,'makeup/Dashbord.html',context)


def Dashbord(request):
    
    products_set= Products.objects.all()
    count_products = products_set.count()

    item_list = [["Products",count_products]]
    type = Type.objects.all()

    for i in type:
        q = i.name
        products_set = Products.objects.filter(
             Q(type__name__icontains = q) |
             Q(Name__icontains = q)    
             ).order_by('-update_time')
        count = products_set.count()
        item_list.append([i,count])
        
        count = len(item_list)
        e = datetime.datetime.now()
        date = e.strftime("%H:%M %a, %B %d")
    context = {
                "item_list":item_list,
                "products_type":type,
                "count":count,
                "date":date,
                 }
    return render(request,'makeup/dashbord.html',context)
