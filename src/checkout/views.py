from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect

import stripe

stripe_pub = settings.STRIPE_PUBLIC_KEY
stripe_secret = settings.STRIPE_SECRET_KEY

stripe.api_key = stripe_secret

# Create your views here.  

# mix box. 
def checkout_mx(request):
    publishKey = settings.STRIPE_PUBLIC_KEY
    if request.method == 'POST':
        token = request.POST['stripeToken']

        try:
            customer = stripe.Customer.create(
                description="This is a Customer Test",
                source=token
            )
            response = redirect('success')
            return response

        except stripe.create.charge as e:
            try:
                charge = stripe.Charge.create(      #added create Charge
                amount=10,
                currency="gbp",
                description="This is a Charge Test",
                source=customer                 #added source customer
            )

        except stripe.error.CardError as e:
            pass

    context = {'publishKey': publishKey}
    template = 'checkout_mx.html'
    return render(request,template,context)



#def checkout_mx(request):
#    publishKey = settings.STRIPE_PUBLIC_KEY
#    if request.method == 'POST':
#        #token = request.POST['stripeToken']    #token deactivated
#        try:
#            Charge = stripe.Charge.create(      #added create Charge
#                amount=10,
#                currency="gbp",
#                description="This is a Test",
#                source=customer                 #added source customer
#            )
#            response = redirect('success')
#            return response
#
#       except stripe.error.CardError as e:
#            pass
#    context = {'publishKey': publishKey}
#    template = 'checkout_mx.html'
#    return render(request,template,context)






# hazelnut + cacao box. 
def checkout_hc(request):
    publishKey = settings.STRIPE_PUBLIC_KEY
    if request.method == 'POST':
        token = request.POST['stripeToken']
        #print_r(_POST)

        try:
            customer = stripe.Customer.create(
                description="This is a Test",
                source=token
            )
            response = redirect('success')
            return response

        except stripe.error.CardError as e:
            pass

    context = {'publishKey': publishKey}
    template = 'checkout_hc.html'
    return render(request,template,context)






# lemon box. 
def checkout_le(request):
    publishKey = settings.STRIPE_PUBLIC_KEY
    if request.method == 'POST':
        token = request.POST['stripeToken']
        #print_r(_POST)

        try:
            customer = stripe.Customer.create(
                description="This is a Test",
                source=token
            )
            response = redirect('success')
            return response

        except stripe.error.CardError as e:
            pass

    context = {'publishKey': publishKey}
    template = 'checkout_le.html'
    return render(request,template,context)



