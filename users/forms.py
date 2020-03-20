from django import forms
from users.models import Account 
#from users.models import Access
from django.forms import TextInput, NumberInput, EmailInput

#from phonenumber_field.formfields import PhoneNumberField
#from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('name', 'phone', 'email', 'address', 'postcode')
        labels = {"address": "Shipping Address"}
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', }),
            'phone': NumberInput(attrs={'class': 'form-control', }),
            'email': EmailInput(attrs={'class': 'form-control', }),
            'address': TextInput(attrs={'class': 'form-control', }),
            'postcode': TextInput(attrs={'class': 'form-control', }),
        }

