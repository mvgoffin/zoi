from django.db import models


#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length = 100, null=True)
    phone = models.BigIntegerField(null=True)
    email = models.EmailField(max_length = 100, null=True) #by default is required
    address = models.CharField(max_length = 100, null=True)
    postcode = models.CharField(max_length = 7, null=True)

class Access(models.Model):
    email = models.EmailField(max_length = 100, null=True) #by default is required

def _unicode_(self):
		return self.id
    

