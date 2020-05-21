'''
Created on May 13, 2020

@author: shamim
'''
from django.forms.models import ModelForm
from customer.models import Customer, FixedProduct, YardProduct, Payment
from django.forms.widgets import DateTimeInput

class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        exclude=('total_due',)        
class FixedProductForm(ModelForm):
    class Meta:
        model=FixedProduct
        fields="__all__"
        
class YardProductForm(ModelForm):
    class Meta:
        model=YardProduct
        exclude=('total_price',)
class PaymentForm(ModelForm):
    class Meta:
        model=Payment
        fields="__all__"
        
    
