from django.contrib import admin

# Register your models here.

from users.models import Account

class accountadmin(admin.ModelAdmin):
    class Meta:
        model = Account

admin.site.register(Account, accountadmin)
