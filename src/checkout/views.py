from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect

import stripe

stripe_pub = settings.STRIPE_PUBLIC_KEY
stripe_secret = settings.STRIPE_SECRET_KEY

stripe.api_key = stripe_secret

# Create your views here.  

# bottle. 
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
            amount=100,
            currency="gbp",
            description="bottle",
            customer=customer                #added source customer
            )
            response = redirect('success')
            return response    
    context = {'publishKey': publishKey}
    template = 'checkout_bottle.html'
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



