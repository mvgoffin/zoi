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

#Register Lemon
def register_lemon(request):
    form = AccountForm(request.POST)

    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    address = request.POST.get('address')
    postcode = request.POST.get('postcode')
    obj = Account.objects.create(name=name, phone=phone, email=email, address=address, postcode=postcode)

    if form.is_valid():

        send_mail(
        'A New Account',
        'From our servers, a new account has been created. Please check it out in the administration console details are as follows' +
        ': name: {}, phone: {}, email: {}, address: {}, postcode: {}'.format(name, phone, email, address, postcode),
        'marco.valgof@gmail.com',
        ['marco.valgof@gmail.com'],
        #fail_silently=False,
        )

        form.save()
        
        response = redirect('checkout_lemon')
        return response
    else:
        form = AccountForm()
    
    return render(request, 'register_lemon.html', {'form': form}) #this is render on HTML

#Register Hazelnut + Cacao
def register_hazelnutcacao(request):
    form = AccountForm(request.POST)

    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    address = request.POST.get('address')
    postcode = request.POST.get('postcode')
    obj = Account.objects.create(name=name, phone=phone, email=email, address=address, postcode=postcode)

    if form.is_valid():

        send_mail(
        'A New Account',
        'From our servers, a new account has been created. Please check it out in the administration console details are as follows' +
        ': name: {}, phone: {}, email: {}, address: {}, postcode: {}'.format(name, phone, email, address, postcode),
        'marco.valgof@gmail.com',
        ['marco.valgof@gmail.com'],
        #fail_silently=False,
        )

        form.save()
        
        response = redirect('checkout_hazelnutcacao')
        return response
    else:
        form = AccountForm()
    
    return render(request, 'register_hazelnutcacao.html', {'form': form}) #this is render on HTML

