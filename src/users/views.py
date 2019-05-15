from django.shortcuts import render 
from django.shortcuts import redirect

from users.forms import AccountForm
from users.models import Account
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
#from users.models import Account

# Create your views here.
def register(request):
    form = AccountForm(request.POST)

    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    address = request.POST.get('address')
    postcode = request.POST.get('postcode')
    obj = Account.objects.create(name=name, phone=phone, email=email, address=address, postcode=postcode)

    if form.is_valid():

        send_mail(
        'A new Account',
        'From our servers, a new account has been created. Please check it out in the administration console details are as follows' +
        ': name: {}, phone: {}, email: {}, address: {}, postcode: {}'.format(name, phone, email, address, postcode),
        'hi@plntprotein.com',
        ['marco@plntprotein.com'],
        #fail_silently=False,
        )

        form.save()
        
        response = redirect('checkout')
        return response
    else:
        form = AccountForm()
    return render(request, 'register.html', {'form': form}) #this is render on HTML


#from users.forms import UserRegisterForm
#from django.http import HttpResponseRedirect
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib import messages
#from django.core.mail import send_mail

#def email(request):
#    subject = 'Thank you for registering to our site'
#    message = ' it  means a world to us '
#    email_from = settings.EMAIL_HOST_USER
#    recipient_list = ['marco@plntprotein.com',]
#    send_mail( subject, message, email_from, recipient_list )
#    return redirect('checkout')




#    send_mail(
#                'A new Account',
#                'You received an new account. Please check it out in the administration console',
#                'hi@plntprotein.com',
#                ['marco@plntprotein.com'],
#                fail_silently=False,
#            )
    


#django Forms
#def register(request):
 #   if request.method == 'POST':
 #       form = UserRegisterForm(request.POST)
  #      if form.is_valid():         #django backend valid data checks
            #obj = Listing()
   #         username = form.cleaned_data.get('username')
    #        phone = form.cleaned_data.get('phone')
     #       email = form.cleaned_data.get('email')
      #      address = form.cleaned_data.get('address')
       #     postcode = form.cleaned_data.get('postcode')
            #cc_myself = form.cleaned_data.get('cc_myself')

            #recipients = ('marco@plntprotein.com')
            #if cc_myself:
            #    recipients.append(email)
            
            #send_mail(phone, email, address, postcode, recipients)

            #messages.success(request, f'Account created for {username}!')
            
  #          form.save()
            
  #          response = redirect('checkout')
  #          return response
  #  else:
  #      form = UserRegisterForm()
  #  return render(request, 'register.html', {'form': form}) #this is render on HTML

