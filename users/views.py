from django.shortcuts import render 
from django.shortcuts import redirect

from users.forms import AccountForm
from users.models import Account
from users.forms import Access

from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from users.models import Account

# Create your views here.
def contact(request):
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')

if request.method == 'POST' and email and name:
    send_mail(subject, content, settings.EMAIL_HOST_USER, ['marco.valgof@gmail.com'], fail_silently=False)
