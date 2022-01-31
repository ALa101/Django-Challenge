from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User
# from datetime import datetime

class connect_us (models.Model):
   user = models.ForeignKey(User,on_delete = models.SET_NULL , null= True)
   topic = models.CharField(max_length=30,help_text='Enter topic') 
   massesg = models.TextField( help_text='Enter massesg')


   #Metadata
#    class Meta :
#        ordering = ['-connect_us']

   #Methods
#    def get_absolute_url(self):
#        return reverse('url', args=[args])

   def __str__(self):
       return self.topic[0:10]


# Create your models here.
# class Brand(models.Model):
#     Name = models.CharField(max_length=20)
#     Orgin = models.CharField(max_length=50)

#     def __str__(self):
#         return self.Name

# class Products(models.Model):
#     Name = models.CharField(max_length=30)
#     Kind = models.CharField
#     Descreption = models.TextField(default= "not found")
#     Exipir_data = models.DateField(default= datetime.now)
#     Price = models.DecimalField(max_digits=10,decimal_places=2)
#     Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.Name



        
    
# class ALa (models.Model):
#    field_name = models.CharField(max_length=20, help_text='Enter field documentation')

#    #Metadata
#    class Meta :
#        ordering = ['-ALa']

#    #Methods
#    def get_absolute_url(self):
#        return reverse('url', args=[args])

#    def __str__(self):
#        return self.field