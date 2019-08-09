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

# Gubel Bottle. 
def checkout_bottle(request):
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
            amount=785,
            currency="gbp",
            description="Gubel Bottle",
            customer=customer                #added source customer
            )
            response = redirect('success')
            return response    
    context = {'publishKey': publishKey}
    template = 'checkout_bottle.html'
    return render(request,template)


# Box. 
def checkout_box(request):
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
            amount=985,
            currency="gbp",
            description="Gubel Box",
            customer=customer                #added source customer
            )
            response = redirect('success')
            return response    
    context = {'publishKey': publishKey}
    template = 'checkout_box.html'
    return render(request,template)




# Gubel SCA.



def checkout_sca():
    publishKey = settings.STRIPE_PUBLIC_KEY
    if request.method == 'POST':
         try:
            intent = stripe.PaymentIntent.create(
            amount=100,
            currency='gbp',
            )
        #except stripe.error.CardError as e:
        #    pass
        #else:
        #charges = stripe.Charge.list(
        #    payment_intent = '{{PAYMENT_INTENT_ID}}',
            # Limit the number of objects to return (the default is 10)
        #    limit = 3,
        #    )
        return render_template('checkout_sca.html', client_secret=intent.client_secret)










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



