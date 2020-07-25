from django.shortcuts import render
from django.shortcuts import redirect

#from profiles.forms import Access (diabling PLNT PROTEIN IG landing page)
#from profiles.forms import AccessForm (diabling PLNT PROTEIN IG landing page)
#from django.core.mail import EmailMessage (diabling PLNT PROTEIN IG landing page)
#from django.core.mail import send_mail (diabling PLNT PROTEIN IG landing page)
from django.conf import settings

# Create your views here.

def home(request):
    context = locals()
    template = 'home.html'
    return render(request,template,context)

def thanks(request):
    context = locals()
    template = 'thanks.html'
    return render(request,template,context)

#1BLives - Rockstar
def zoi_home(request):
    context = locals()
    template = 'zoi_home.html'
    return render(request,template,context)

def zoi_about(request):
    context = locals()
    template = 'zoi_about.html'
    return render(request,template,context)

def zoi_registration(request):
    context = locals()
    template = 'zoi_registration.html'
    return render(request,template,context)

def zoi_laptops(request):
    context = locals()
    template = 'zoi_laptops.html'
    return render(request,template,context)
    
def zoi_product(request):
    context = locals()
    template = 'zoi_product.html'
    return render(request,template,context)

def zoi_checkout(request):
    context = locals()
    template = 'zoi_checkout.html'
    return render(request,template,context)

def zoi_thankyou(request):
    context = locals()
    template = 'zoi_thankyou.html'
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
def bt_cx(request):
    context = locals()
    template = 'bt_cx.html'
    return render(request,template,context)
    
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

def vfepisodes(request):
    context = locals()
    template = 'vfepisodes.html'
    return render(request,template,context)

def vftimeline(request):
    context = locals()
    template = 'vftimeline.html'
    return render(request,template,context)

#greencourt technologies
def gclogin(request):
    context = locals()
    template = 'gclogin.html'
    return render(request,template,context)

def gcpage(request):
    context = locals()
    template = 'gcpage.html'
    return render(request,template,context)

def pagevf_mike(request):
    context = locals()
    template = 'pagevf_mike.html'
    return render(request,template,context)


#def pagevf_ariana(request):
 #   context = locals()
  #  template = 'pagevf_ariana.html'
   # return render(request,template,context)



