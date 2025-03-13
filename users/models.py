from django.db import models
from django.contrib.auth.models import AbstractUser
from store.models import *





class User(AbstractUser):
    
    company = models.ForeignKey(company, on_delete=models.CASCADE, blank = True, null = True)
    office_location = models.ForeignKey(office_location, on_delete=models.CASCADE, blank = True, null = True)
    password_r = models.CharField(max_length=50, null = True, blank = True)
    date_joined =  models.DateField(default=datetime.now, blank=True, null=True)
    balance = models.FloatField(default = 0)
    