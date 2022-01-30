import re
from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return render(request,'pages/index.html',{'name':'ALa'})
    # return HttpResponse("Ala HI dfdsfasdf")

def index2(requset):
    return render(requset,'pages2/index2.html')    

# Create your views here.
