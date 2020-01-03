from django.shortcuts import render
from django.shortcuts import redirect

#from profiles.forms import Access (diabling PLNT PROTEIN IG landing page)
#from profiles.forms import AccessForm (diabling PLNT PROTEIN IG landing page)
#from django.core.mail import EmailMessage (diabling PLNT PROTEIN IG landing page)
#from django.core.mail import send_mail (diabling PLNT PROTEIN IG landing page)
from django.conf import settings

# Create your views here.

#Marco for Telefonica Views

def home(request):
    context = locals()
    template = 'home.html'
    return render(request,template,context)

#Marco for Telefonica Test
def home2(request):
    context = locals()
    template = 'home2.html'
    return render(request,template,context)

#(3 pages) PAYG+ + EC + NC Product Views

def payg_plus(request):
    context = locals()
    template = 'payg_plus.html'
    return render(request,template,context)

def payg_plus_ec(request):
    context = locals()
    template = 'payg_plus_ec.html'
    return render(request,template,context)

def payg_plus_nc(request):
    context = locals()
    template = 'payg_plus_nc.html'
    return render(request,template,context)



#(10 pages) Checkout Account Views

#Existing Customers Account and Payment Pages
#Existing Customers Account 
def checkout_ec_account_0(request):
    context = locals()
    template = 'checkout_ec_account_0.html'
    return render(request,template,context)

def checkout_ec_account_3(request):
    context = locals()
    template = 'checkout_ec_account_3.html'
    return render(request,template,context)

def checkout_ec_account_6(request):
    context = locals()
    template = 'checkout_ec_account_6.html'
    return render(request,template,context)

def checkout_ec_account_10(request):
    context = locals()
    template = 'checkout_ec_account_10.html'
    return render(request,template,context)

def checkout_ec_account_20(request):
    context = locals()
    template = 'checkout_ec_account_20.html'
    return render(request,template,context)

#Exiting Customers Payment
def checkout_ec_payment_0(request):
    context = locals()
    template = 'checkout_ec_payment_0.html'
    return render(request,template,context)

def checkout_ec_payment_3(request):
    context = locals()
    template = 'checkout_ec_payment_3.html'
    return render(request,template,context)

def checkout_ec_payment_6(request):
    context = locals()
    template = 'checkout_ec_payment_6.html'
    return render(request,template,context)

def checkout_ec_payment_10(request):
    context = locals()
    template = 'checkout_ec_payment_10.html'
    return render(request,template,context)

def checkout_ec_payment_20(request):
    context = locals()
    template = 'checkout_ec_payment_20.html'
    return render(request,template,context)



#New Customers Account and Payment Pages
def checkout_nc_account_0(request):
    context = locals()
    template = 'checkout_nc_account_0.html'
    return render(request,template,context)

def checkout_nc_account_3(request):
    context = locals()
    template = 'checkout_nc_account_3.html'
    return render(request,template,context)

def checkout_nc_account_6(request):
    context = locals()
    template = 'checkout_nc_account_6.html'
    return render(request,template,context)

def checkout_nc_account_10(request):
    context = locals()
    template = 'checkout_nc_account_10.html'
    return render(request,template,context)

def checkout_nc_account_20(request):
    context = locals()
    template = 'checkout_nc_account_20.html'
    return render(request,template,context)

#Payments
def checkout_nc_payment_0(request):
    context = locals()
    template = 'checkout_nc_payment_0.html'
    return render(request,template,context)

def checkout_nc_payment_3(request):
    context = locals()
    template = 'checkout_nc_payment_3.html'
    return render(request,template,context)

def checkout_nc_payment_6(request):
    context = locals()
    template = 'checkout_nc_payment_6.html'
    return render(request,template,context)

def checkout_nc_payment_10(request):
    context = locals()
    template = 'checkout_nc_payment_10.html'
    return render(request,template,context)

def checkout_nc_payment_20(request):
    context = locals()
    template = 'checkout_nc_payment_20.html'
    return render(request,template,context)




#(2 pages) Success New and Existing Customers
def payg_plus_ec_success(request):
    context = locals()
    template = 'payg_plus_ec_success.html'
    return render(request,template,context)

def payg_plus_nc_success(request):
    context = locals()
    template = 'payg_plus_nc_success.html'
    return render(request,template,context)








#Test pages
def test(request):
    context = locals()
    template = 'test.html'
    return render(request,template,context)

#------------PROJECT LIVING PLANTS AND GUBEL-----------------#
def about(request):
    context = locals()
    template = 'about.html'
    return render(request,template,context)

def success(request):
    context = locals()
    template = 'success.html'
    return render(request,template,context)

def successaccount(request):
    context = locals()
    template = 'success-account.html'
    return render(request,template,context)

def termsofservice(request):
    context = locals()
    template = 'terms-of-service.html'
    return render(request,template,context)

def privacypolicy(request):
    context = locals()
    template = 'privacy-policy.html'
    return render(request,template,context)

def smspolicy(request):
    context = locals()
    template = 'sms-policy.html'
    return render(request,template,context)

def hometest(request):
    context = locals()
    template = 'hometest.html'
    return render(request,template,context)

def calm_jar(request):
    context = locals()
    template = 'calm_jar.html'
    return render(request,template,context)

def skincare_jar(request):
    context = locals()
    template = 'skincare_jar.html'
    return render(request,template,context)

def navbar(request):
    context = locals()
    template = 'navbar.html'
    return render(request,template,context)

#def code_granted(request):
#    context = locals()
#    template = 'code_granted.html'
#    return render(request,template,context)

#Disabling Home PLNT PROTEIN Landing Page
#def home(request):
#    form = AccessForm(request.POST)

#    email = request.POST.get('email')
#    obj = Access.objects.create(email=email)

#    if form.is_valid():

#        send_mail(
#        'A new LEAD',
#        'From our servers, a new LEAD has been created.' +
#        ': email: {}'.format(email),
#        'hi@plntprotein.com',
#        ['marco@plntprotein.com'],
        #fail_silently=False,
#        )

#        form.save()
        
#        response = redirect('code_granted')
#        return response
#    else:
#        form = AccessForm()
    
     #context = {'form': form}
     #template = 'register_mx.html'
     #return render(request,template,context)
#    return render(request, 'home.html', {'form': form}) #this is render on HTML

