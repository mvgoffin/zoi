from django.shortcuts import render
from django.shortcuts import redirect

#from profiles.forms import Access (diabling PLNT PROTEIN IG landing page)
#from profiles.forms import AccessForm (diabling PLNT PROTEIN IG landing page)
#from django.core.mail import EmailMessage (diabling PLNT PROTEIN IG landing page)
#from django.core.mail import send_mail (diabling PLNT PROTEIN IG landing page)
from django.conf import settings

# Create your views here.

#Altered.ai - Views

def home(request):
    context = locals()
    template = 'home.html'
    return render(request,template,context)

def login_vf(request):
    context = locals()
    template = 'login_vf.html'
    return render(request,template,context)

def vodafone(request):
    context = locals()
    template = 'vodafone.html'
    return render(request,template,context)



