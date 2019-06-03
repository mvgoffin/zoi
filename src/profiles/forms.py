from django import forms 
from profiles.models import Access
from django.forms import TextInput, NumberInput, EmailInput

#Disabling Home PLNT PROTEIN Landing Page
#class AccessForm(forms.ModelForm):
#    class Meta:
#        model = Access
#        fields = ('email',)
#        widgets = {
#            'email': EmailInput(attrs={'class': 'form-control', }),
#        }