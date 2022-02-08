from datetime import datetime
from email.policy import default
from itertools import product
from pickle import TRUE
from tkinter import N
from turtle import update
from django.db import models

from brand.models import Brand



# import Brand

class Type (models.Model):
#    id_type = models.IntegerField(default=0) 
   name = models.CharField(max_length=20,default="no Type" ,help_text='Enter type name ')
  
   def __str__(self):
       return self.name

       
# Create your models here.
class Products(models.Model):
    Name = models.CharField(max_length=30)
    Descreption = models.TextField(max_length=200, default="")
    Exipir_data = models.DateField(default= datetime.now)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null= True)
    image = models.ImageField(upload_to="image/products/%y/%m/%d", null = True, blank = True, default ="image/products/wk21_brushes_02.jpg" )
    crate_time = models.DateTimeField(auto_now_add= True, null=True)
    update_time = models.DateTimeField(auto_now = True, null= True)

    
    def __str__(self):
        return self.Name

