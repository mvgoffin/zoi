from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect
from thecheckout import urls

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

import requests
import json

import stripe

stripe_pub = settings.STRIPE_PUBLIC_KEY
stripe_secret = settings.STRIPE_SECRET_KEY

stripe.api_key = stripe_secret

# Create your views here.  

# calm Starter Bundle. 
def checkout_calm_jar(request):
    publishKey = settings.STRIPE_PUBLIC_KEY
    if request.method == 'POST':
        token = request.POST['stripeToken']
        try:
            customer = stripe.Customer.create(
                description="new customer",
                source=token
            )
        except stripe.error.CardError as e:
           pass
        else:
            charge = stripe.Charge.create(      #added create Charge
            amount=1000,
            currency="gbp",
            description="calm - 2-Week Starter Bundle",
            customer=customer                #added source customer
            )
            response = redirect('success')
            return response    
    context = {'publishKey': publishKey}
    template = 'checkout_calm_jar.html'
    return render(request,template)


# skincare starter bundle. 
def checkout_skincare_jar(request):
    publishKey = settings.STRIPE_PUBLIC_KEY
    if request.method == 'POST':
        token = request.POST['stripeToken']
        try:
            customer = stripe.Customer.create(
                description="new customer",
                source=token
            )
        except stripe.error.CardError as e:
           pass
        else:
            charge = stripe.Charge.create(      #added create Charge
            amount=1000,
            currency="gbp",
            description="skincare - 2-Week Starter Bundle",
            customer=customer                #added source customer
            )
            response = redirect('success')
            return response    
    context = {'publishKey': publishKey}
    template = 'checkout_skincare_jar.html'
    return render(request,template)


# calm + skincare starter bundle. 
def checkout_calm_skincare_jar(request):
    publishKey = settings.STRIPE_PUBLIC_KEY
    if request.method == 'POST':
        token = request.POST['stripeToken']
        try:
            customer = stripe.Customer.create(
                description="new customer",
                source=token
            )
        except stripe.error.CardError as e:
           pass
        else:
            charge = stripe.Charge.create(      #added create Charge
            amount=2000,
            currency="gbp",
            description="calm + skincare - 2-Week Starter Bundle",
            customer=customer                #added source customer
            )
            response = redirect('success')
            return response    
    context = {'publishKey': publishKey}
    template = 'checkout_calm_skincare_jar.html'
    return render(request,template)




# Gubel SCA.



def checkout_sca(request):
    publishKey = settings.STRIPE_PUBLIC_KEY
    intent = None
    if request.method == 'POST':
         intent = stripe.PaymentIntent.create(
            amount=100,
            currency='gbp',
            )
        ##response = redirect('success')
        ##return response
        #except stripe.error.CardError as e:
        #    pass
    context = {'publishKey': publishKey}
    template = 'checkout_sca.html'
    #client_secret=intent.client_secret
    #return render(request,template, client_secret=intent.client_secret)
    return render(request,template)










# mix box. 
def checkout_mx(request):
    publishKey = settings.STRIPE_PUBLIC_KEY
    if request.method == 'POST':
        token = request.POST['stripeToken']
        try:
            customer = stripe.Customer.create(
                description="new customer",
                source=token
            )
        except stripe.error.CardError as e:
           pass
        else:
            charge = stripe.Charge.create(      #added create Charge
            amount=100,
            currency="gbp",
            description="mix box",
            customer=customer                #added source customer
            )
            response = redirect('success')
            return response    
    context = {'publishKey': publishKey}
    template = 'checkout_mx.html'
    return render(request,template)



# hazelnut + cacao box. 
def checkout_hc(request):
    publishKey = settings.STRIPE_PUBLIC_KEY
    if request.method == 'POST':
        token = request.POST['stripeToken']
        try:
            customer = stripe.Customer.create(
                description="new customer",
                source=token
            )
        except stripe.error.CardError as e:
           pass
        else:
            charge = stripe.Charge.create(      #added create Charge
            amount=100,
            currency="gbp",
            description="hazelnut + cacao box",
            customer=customer                #added source customer
            )
            response = redirect('success')
            return response    
    context = {'publishKey': publishKey}
    template = 'checkout_hc.html'
    return render(request,template)






# lemon box. 
def checkout_le(request):
    publishKey = settings.STRIPE_PUBLIC_KEY
    if request.method == 'POST':
        token = request.POST['stripeToken']
        try:
            customer = stripe.Customer.create(
                description="new customer",
                source=token
            )
        except stripe.error.CardError as e:
           pass
        else:
            charge = stripe.Charge.create(      #added create Charge
            amount=100,
            currency="gbp",
            description="lemon box",
            customer=customer                #added source customer
            )
            response = redirect('success')
            return response    
    context = {'publishKey': publishKey}
    template = 'checkout_le.html'
    return render(request,template)



