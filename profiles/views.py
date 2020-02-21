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

def search(request):
    context = locals()
    template = 'search.html'
    return render(request,template,context)

def lemon(request):
    context = locals()
    template = 'lemon.html'
    return render(request,template,context)

def hazelnutcacao(request):
    context = locals()
    template = 'hazelnutcacao.html'
    return render(request,template,context)

def termsofservice(request):
    context = locals()
    template = 'termsofservice.html'
    return render(request,template,context)

def privacypolicy(request):
    context = locals()
    template = 'privacypolicy.html'
    return render(request,template,context)

def textpolicy(request):
    context = locals()
    template = 'textpolicy.html'
    return render(request,template,context)

def thankyou(request):
    context = locals()
    template = 'thankyou.html'
    return render(request,template,context)



def register_lemon(request):
    context = locals()
    template = 'register_lemon.html'
    return render(request,template,context)

def register_hazelnutcacao(request):
    context = locals()
    template = 'register_hazelnutcacao.html'
    return render(request,template,context)


def checkout_lemon(request):
    context = locals()
    template = 'checkout_lemon.html'
    return render(request,template,context)

def checkout_hazelnutcacao(request):
    context = locals()
    template = 'checkout_hazelnutcacao.html'
    return render(request,template,context)




