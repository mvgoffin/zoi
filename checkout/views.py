from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect
from zoi import urls

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

import requests
import json

import stripe



# Create your views here.  
