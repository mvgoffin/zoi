"""zoi URL Configuration

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

#from zoi.views import home, send_push #web-push


urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    
    
    #----Zoi Marketplace----#
    path('zoi_home/', views.zoi_home, name='zoi_home'),
    path('zoi_about/', views.zoi_about, name='zoi_about'),
    path('zoi_registration/', views.zoi_registration, name='zoi_registration'),
    path('zoi_laptops/', views.zoi_laptops, name='zoi_laptops'),
    path('zoi_product/', views.zoi_product, name='zoi_product'),
    path('zoi_checkout/', views.zoi_checkout, name='zoi_checkout'),
    path('zoi_thankyou/', views.zoi_thankyou, name='zoi_thankyou'),
]
