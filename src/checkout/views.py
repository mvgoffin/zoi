from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect

import stripe

stripe_pub = settings.STRIPE_PUBLIC_KEY
stripe_secret = settings.STRIPE_SECRET_KEY

stripe.api_key = stripe_secret

# Create your views here.  

def checkout(request):
    publishKey = settings.STRIPE_PUBLIC_KEY
    if request.method == 'POST':
        token = request.POST['stripeToken']

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
    template = 'checkout.html'
    return render(request,template,context)



