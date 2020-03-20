from django import forms 
#from profiles.models import Access (diabling PLNT PROTEIN IG landing page)
from django.forms import TextInput, NumberInput, EmailInput

#Disabling Home 
class AccessForm(forms.ModelForm):
    class Meta:
        model = Access
        fields = ('email',)
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control', }),
        }