from django.shortcuts import render

# Create your views here.

def home(request ):
   
    
    return render(request,'makeup/home.html')
# def navbar(request):
#     return render(request,'makeup/navbar.html' )


# def makeup_choes(request):
#     return render(request,'makeup/makeup.html')


# def type_item(request, type_item):
#     # print (type_item)
#     return render(request,'makeup/makeup.html')

