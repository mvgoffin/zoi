#from django.shortcuts import render 
#from django.shortcuts import redirect

#from users.forms import AccountForm
#from users.models import Account
#from users.forms import Access

#from django.core.mail import EmailMessage
#from django.core.mail import send_mail
#from django.conf import settings
#from users.models import Account

# Create your views here.
#def contact(request):
#    name = request.POST.get('name', '')
#    email = request.POST.get('email', '')

#if request.method == 'POST' and email and name:
#    send_mail(subject, content, settings.EMAIL_HOST_USER, ['marco.valgof@gmail.com'], fail_silently=False)


#from django.http import HttpResponseRedirect
#from django.shortcuts import render
#from users.forms import NameForm

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    if request.method == 'POST':
        name = request.POST['name']

        send_mail('Contact From', 
        name, 
        settings.EMAIL_HOST_USER, 
        ['marco.valgof@gmail.com'], 
        fail_silently=False)
    return render(request, 'app/home.html')


#def email(request):
#    subject = 'Thank you for registering to our site'
#    message = ' it  means a world to us '
#    email_from = settings.EMAIL_HOST_USER
#    recipient_list = ['marco.valgof@gmail.com',]
#    send_mail( your_name, your-email )
#    return redirect('redirect to a new page')