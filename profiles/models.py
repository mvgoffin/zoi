from django.db import models

# Create your models here.

Disabling Home PLNT PROTEIN Landing Page
class Access(models.Model):
    email = models.EmailField(max_length = 100, null=True) #by default is required
	

		