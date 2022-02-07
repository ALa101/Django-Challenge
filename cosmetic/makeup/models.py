
from django.db import models
from django.contrib.auth.models import User
# from datetime import datetime


class connect_us (models.Model):
   user = models.ForeignKey(User,on_delete = models.CASCADE)
   topic = models.CharField(max_length=30,help_text='Enter topic') 
   massesg = models.TextField( help_text='Enter massesg')
   created = models.DateTimeField(auto_now=True)

   def __str__(self):
       return self.topic[0:10]
   



