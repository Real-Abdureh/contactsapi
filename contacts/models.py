from django.db import models
from django.contrib.auth.models import User



class contacts(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=30)
    First_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    contact_picture = models.URLField(null=True)
    is_favorite = models.BooleanField(default=True)

# Create your models here.
