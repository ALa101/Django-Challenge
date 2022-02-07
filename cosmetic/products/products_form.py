from django.forms import ModelForm
from .models import Products



class product_Form(ModelForm):
    """Form definition for edit_product_."""
    class Meta:
        model = Products
        fields = '__all__'
