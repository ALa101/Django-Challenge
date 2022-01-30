from datetime import datetime
from django.db import models

from brand.models import Brand


# import Brand


# Create your models here.
class Products(models.Model):
    Name = models.CharField(max_length=30)
    Kind = models.CharField
    Descreption = models.TextField(default= "not found")
    Exipir_data = models.DateField(default= datetime.now)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Name