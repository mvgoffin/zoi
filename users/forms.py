from django import forms
#from users.models import Account 
#from users.models import Access
#from django.forms import TextInput, NumberInput, EmailInput

#from phonenumber_field.formfields import PhoneNumberField
#from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm

#class AccountForm(forms.ModelForm):
#    class Meta:
#        model = Account
#        fields = ('name', 'email')
        #labels = {"address": "Shipping Address"}
#        widgets = {
#            'name': TextInput(attrs={'class': 'form-control', }),
#            'email': EmailInput(attrs={'class': 'form-control', }),
#        }

from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_email = forms.CharField(label='Your email', max_length=100)

