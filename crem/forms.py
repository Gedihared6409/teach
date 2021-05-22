from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from . import models

from .models import Order,Customer,repairAsset

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
class RepairAssetForm(forms.ModelForm):
    class Meta :
        model = Customer
        fields =  ['catego']
		
class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

# class CreateUserForm(UserCreationForm):
#     is_manager = models.BooleanField(default=False)
#     is_employee = models.BooleanField(default=False)
#     class Meta:
#         model = User
#         fields = '__all__'

