from django.contrib import admin

# Register your models here.

from users.models import Account

#Disabling Home PLNT PROTEIN Landing Page (not yet)
class accountadmin(admin.ModelAdmin):
    class Meta:
        model = Account

admin.site.register(Account, accountadmin)
