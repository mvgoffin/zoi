from django import forms

class contactformemail(forms.Form):
    fromemail=forms.EmailField(required=True)
    subject=form.CharField(required=True)
    message=form.CharField(required=True)
    