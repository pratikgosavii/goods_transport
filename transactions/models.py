from django.db import models

# Create your models here.



from users.models import User
from datetime import datetime, timezone
from store.models import *


ex_for = (
    ('for','for'),
    ('ex', 'ex'),
   
)

mode = (
    ('cash','cash'),
    ('online', 'online'),
   
)

class builty(models.Model):

    company = models.ForeignKey(company , on_delete=models.CASCADE, related_name='sdwe')
    builty_no = models.CharField(max_length=50)
    DC_date = models.DateField(auto_now_add=False)
    truck_details = models.ForeignKey(truck_details , on_delete=models.CASCADE, related_name='sdsdsc')
    truck_owner = models.ForeignKey(truck_owner , on_delete=models.CASCADE, related_name='cxcdfdfvd')
    consignor = models.ForeignKey(consignor , on_delete=models.CASCADE, related_name='wdsfgv')
    petrol_pump = models.ForeignKey(petrol_pump , null = True, blank = True, on_delete=models.CASCADE, related_name='wdsfgv')
    station_from = models.ForeignKey(station , on_delete=models.CASCADE, related_name='sdsdsdssdsdsdcs')
    station_to = models.ForeignKey(station , on_delete=models.CASCADE, related_name='dvccxcred')
    consignee = models.CharField(max_length=50)
    taluka = models.ForeignKey(taluka, on_delete=models.CASCADE, related_name='sdscsc')
    district = models.ForeignKey(district, on_delete=models.CASCADE, related_name='sddcxfw')
    onaccount = models.ForeignKey(onaccount , on_delete=models.CASCADE, related_name='wfdfgfdgv')
    article = models.ForeignKey(article , on_delete=models.CASCADE, related_name='dffdcxvc')
    bags = models.FloatField()
    delivery_no = models.FloatField()
    mobile_no = models.FloatField(null = True, blank = True, default=0)
    ex_for = models.CharField(max_length=50, choices=ex_for, default="for")
    mode = models.CharField(max_length=50, choices=mode, default="cash")
    note = models.CharField(null = True, blank = True, max_length=50)
    rate = models.FloatField(null = True, blank = True, default=0)
    mt = models.FloatField(null = True, blank = True, default=0)
    freight = models.FloatField(null = True, blank = True, default=0)
    less_advance = models.FloatField(null = True, blank = True, default=0)
    less_tds = models.FloatField(null = True, blank = True, default=0)
    balance = models.FloatField(null = True, blank = True, default=0)
    diesel = models.FloatField(default=0.0)
    editable = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.company.company_name

   

class ack(models.Model):

    builty = models.ForeignKey(builty, on_delete=models.CASCADE, related_name='have_ack')
    challan_number = models.CharField(max_length=50)
    challan_date = models.DateField(blank = True, null = True, auto_now_add=False)

    def __str__(self):
        return self.builty.builty_no

class request_edit(models.Model):

    builty = models.ForeignKey(builty, on_delete=models.CASCADE, related_name="has_request")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    history = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
   

class sub_trip(models.Model):

    builty = models.ForeignKey(builty, on_delete=models.CASCADE, related_name = 'sub_trip_is')
    station_from = models.ForeignKey(station , on_delete=models.CASCADE, related_name='sdfdcxcde')
    station_to = models.ForeignKey(station , on_delete=models.CASCADE, related_name='dfdcxcfbgefwd')
    diesel = models.FloatField(default=0.0)
    note = models.CharField(max_length=50)

    def __str__(self):
        return self.builty.builty_no



   
