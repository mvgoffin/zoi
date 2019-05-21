from django.db import models

# Create your models here.
class Access(models.Model):
    email = models.EmailField(max_length = 100, null=True) #by default is required
	

		