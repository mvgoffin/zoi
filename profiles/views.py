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

#LSEG
def loginlseg(request):
    context = locals()
    template = 'loginlseg.html'
    return render(request,template,context)

def pagelseg(request):
    context = locals()
    template = 'pagelseg.html'
    return render(request,template,context)

def pagelseg_mike(request):
    context = locals()
    template = 'pagelseg_mike.html'
    return render(request,template,context)

#BP
def loginbp(request):
    context = locals()
    template = 'loginbp.html'
    return render(request,template,context)

def pagelseg(request):
    context = locals()
    template = 'pagebp.html'
    return render(request,template,context)

def pagelseg_mike(request):
    context = locals()
    template = 'pagebp_mike.html'
    return render(request,template,context)



def loginvf_john(request):
    context = locals()
    template = 'loginvf_john.html'
    return render(request,template,context)

def pagevf_john(request):
    context = locals()
    template = 'pagevf_john.html'
    return render(request,template,context)

def pagevf_ariana(request):
    context = locals()
    template = 'pagevf_ariana.html'
    return render(request,template,context)



