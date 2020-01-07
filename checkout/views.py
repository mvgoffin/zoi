from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect
from plntprotein import urls

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
#def checkout_calm_jar(request):
#    publishKey = settings.STRIPE_PUBLIC_KEY
#    if request.method == 'POST':
#        token = request.POST['stripeToken']
#        try:
#            customer = stripe.Customer.create(
#                description="new customer",
#                source=token
#            )
#        except stripe.error.CardError as e:
#           pass
#        else:
#            charge = stripe.Charge.create(      #added create Charge
#            amount=1000,
#            currency="gbp",
#            description="calm - 2-Week Starter Bundle",
#            customer=customer                #added source customer
#            )
#            response = redirect('success')
#            return response    
#    context = {'publishKey': publishKey}
#    template = 'checkout_calm_jar.html'
#    return render(request,template)
