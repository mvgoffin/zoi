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


from django.http import HttpResponseRedirect
from django.shortcuts import render

from users.forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'thanks.html', {'form': form})