"""dak URL Configuration

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

#from dak.views import home, send_push #web-push


urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('search/', views.search, name='search'),
    
    path('thankyou/', views.thankyou, name='thankyou'),
    
    path('lemon/', views.lemon, name='lemon'),
    path('hazelnutcacao/', views.hazelnutcacao, name='hazelnutcacao'),
    
    path('termsofservice/', views.termsofservice, name='termsofservice'),
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
    path('textpolicy/', views.textpolicy, name='textpolicy'),

    path('register_lemon/', views.register_lemon, name='register_lemon'),
    path('register_hazelnutcacao/', views.register_hazelnutcacao, name='register_hazelnutcacao'),

    path('checkout_lemon/', views.checkout_lemon, name='checkout_lemon'),
    path('checkout_hazelnutcacao/', views.checkout_hazelnutcacao, name='checkout_hazelnutcacao'),
   
    
]
