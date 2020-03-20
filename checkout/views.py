from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect
from alteredai import urls

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

import requests
import json

import stripe

stripe_pub = settings.STRIPE_PUBLIC_KEY
stripe_secret = settings.STRIPE_SECRET_KEY

stripe.api_key = stripe_secret

# Create your views here.  
