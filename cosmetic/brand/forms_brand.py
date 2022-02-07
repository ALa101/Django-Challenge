
from django import forms
from .models import Brand


class add_brand_form(forms.ModelForm):   #Metadata
   class Meta:
       model = Brand
       fields = '__all__'


