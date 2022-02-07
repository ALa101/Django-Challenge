
from django.forms import ModelForm
from .models import connect_us


class connect_us_form(ModelForm): 
   class Meta:
       model = connect_us
       fields = '__all__'

