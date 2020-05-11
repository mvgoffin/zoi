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

#BT
def btlogin(request):
    context = locals()
    template = 'btlogin.html'
    return render(request,template,context)

def btpage(request):
    context = locals()
    template = 'btpage.html'
    return render(request,template,context)

def btpage_mike(request):
    context = locals()
    template = 'btpage_mike.html'
    return render(request,template,context)

#BP
def bplogin(request):
    context = locals()
    template = 'bplogin.html'
    return render(request,template,context)

def bppage(request):
    context = locals()
    template = 'bppage.html'
    return render(request,template,context)

def bppage_mike(request):
    context = locals()
    template = 'bppage_mike.html'
    return render(request,template,context)

#Vodafone
def loginvf(request):
    context = locals()
    template = 'loginvf.html'
    return render(request,template,context)

def pagevf(request):
    context = locals()
    template = 'pagevf.html'
    return render(request,template,context)

def pagevf_mike(request):
    context = locals()
    template = 'pagevf_mike.html'
    return render(request,template,context)




#def pagevf_ariana(request):
 #   context = locals()
  #  template = 'pagevf_ariana.html'
   # return render(request,template,context)



