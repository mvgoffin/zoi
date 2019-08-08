from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect
from thecheckout import urls

from django.http import JsonResponse
#from flask import jsonify

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

def checkout_sca(request):
    #publishKey = settings.STRIPE_PUBLIC_KEY
    data = request.get_json()
    intent = None

  try:
    if request.method == 'POST' and 'payment_method_id' in data:
      # Create the PaymentIntent
      intent = stripe.PaymentIntent.create(
        payment_method = data['payment_method_id'],
        amount = 1099,
        currency = 'gbp',
        confirmation_method = 'manual',
        confirm = True,
      )
    elif 'payment_intent_id' in data:
      intent = stripe.PaymentIntent.confirm(data['payment_intent_id'])
  except stripe.error.CardError as e:
    # Display error on client
    return json.dumps({'error': e.user_message}), 200

  return generate_payment_response(intent)

def generate_payment_response(intent):
  # Note that if your API version is before 2019-02-11, 'requires_action'
  # appears as 'requires_source_action'.
  if intent.status == 'requires_action' and intent.next_action.type == 'use_stripe_sdk':
    # Tell the client to handle the action
    return json.dumps({
      'requires_action': True,
      'payment_intent_client_secret': intent.client_secret,
    }), 200
  elif intent.status == 'succeeded':
    # The payment didn’t need any additional actions and completed!
    # Handle post-payment fulfillment
    return json.dumps({'success': True}), 200
  else:
    # Invalid status
    return json.dumps({'error': 'Invalid PaymentIntent status'}), 500











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



