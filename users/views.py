from django.shortcuts import render 
from django.shortcuts import redirect

from users.forms import AccountForm
from users.models import Account
#from users.forms import Access
#from users.forms import AccessForm

from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
#from users.models import Account

# Create your views here.

