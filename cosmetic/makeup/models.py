from django.db import models
# from datetime import datetime

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