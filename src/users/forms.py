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

class AccessForm(forms.ModelForm):
    class Meta:
        model = Access
        fields = ('email',)
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control', }),
        }
        










#def save(self, *args, **kwargs):
    #print("HI")
    #return super(AccountForm, self).save(*args, **kwargs)

#class UserRegisterForm(UserCreationForm): #add the Fields on the form
#    phone = forms.CharField()
 #   email = forms.EmailField() #by default is required
  #  address = forms.CharField(label='Shipping Address', max_length=100, help_text="We ship only to the UK.")
   # postcode = forms.CharField(max_length=7)

    #class Meta:
     #   model = User
      #  fields = ['username', 'phone', 'email', 'address', 'postcode'] #add the fields to be shown on the form and order


