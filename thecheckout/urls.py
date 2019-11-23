"""thecheckout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from profiles import views
from checkout import views as checkout_views
from users import views as user_views

#from thecheckout.views import home, send_push #web-push


urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    #path('admin/', admin.site.urls),
    #path('home/', views.home, name='home'),
    #path('about/', views.about, name='about'),
    #path('calm_jar/', views.calm_jar, name='calm-jar'),
    #path('skincare_jar/', views.skincare_jar, name='skincare-jar'),
    #path('register_calm_jar/', user_views.register_calm_jar, name='register_calm_jar'),
    #path('register_skincare_jar/', user_views.register_skincare_jar, name='register_skincare_jar'),
    #path('register_calm_skincare_jar/', user_views.register_calm_skincare_jar, name='register_calm_skincare_jar'),
    #path('checkout_calm_jar/', checkout_views.checkout_calm_jar, name='checkout_calm_jar'),
    #path('checkout_skincare_jar/', checkout_views.checkout_skincare_jar, name='checkout_skincare_jar'),
    #path('checkout_calm_skincare_jar/', checkout_views.checkout_calm_skincare_jar, name='checkout_calm_skincare_jar'),
    #path('refill/', checkout_views.refill, name='refill'),
    #path('register_box/', user_views.register_box, name='register_box'),
    #path('register_mx/', user_views.register_mx, name='register_mx'),
    #path('register_le/', user_views.register_le, name='register_le'),
    #path('register_hc/', user_views.register_hc, name='register_hc'),
    #path('access_code/', user_views.access_code, name='access_code'),
    #path('checkout_jar/', checkout_views.checkout_jar, name='checkout_jar'),
    #path('checkout_box/', checkout_views.checkout_box, name='checkout_box'),
    #path('checkout_sca/', checkout_views.checkout_sca, name='checkout_sca'),
    #path('checkout_box/', checkout_views.checkout_box, name='checkout_box'),
    #path('checkout_mx/', checkout_views.checkout_mx, name='checkout_mx'),
    #path('checkout_le/', checkout_views.checkout_le, name='checkout_le'),
    #path('checkout_hc/', checkout_views.checkout_hc, name='checkout_hc'),
    #path('terms-of-service/', views.termsofservice, name='terms-of-service'),
    #path('privacy-policy/', views.privacypolicy, name='privacy-policy'),
    #path('sms-policy/', views.smspolicy, name='sms-policy'),
    path('paygplus/', views.paygplus, name='paygplus'),
    path('checkout-account-0/', views.checkout-account-0, name='checkout-account-0'),
    path('checkout-account-3/', views.checkout-account-3, name='checkout-account-3'),
    path('checkout-account-6/', views.checkout-account-6, name='checkout-account-6'),
    path('checkout-account-10/', views.checkout-account-10, name='checkout-account-10'),
    path('checkout-account-20/', views.checkout-account-20, name='checkout-account-20'),
    path('checkout-payment-0/', views.checkout-payment-0, name='checkout-payment-0'),
    path('checkout-payment-3/', views.checkout-payment-3, name='checkout-payment-3'),
    path('checkout-payment-6/', views.checkout-payment-6, name='checkout-payment-6'),
    path('checkout-payment-10/', views.checkout-payment-10, name='checkout-payment-10'),
    path('checkout-payment-20/', views.checkout-payment-20, name='checkout-payment-20'),
    path('payg-plus-success/', views.payg-plus-success, name='payg-plus-success'),
    #path('hometest/', views.hometest, name='hometest'),
    #path('code_granted/', views.code_granted, name='code_granted'),
    
#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#web-push
    #path('', home),
    #path('send_push', send_push),
    #path('webpush/', include('webpush.urls')),
]
