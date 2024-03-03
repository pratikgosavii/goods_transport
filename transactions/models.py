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

mode1 = (
    ('cash','cash'),
    ('online', 'online'),
   
)

class builty(models.Model):

    company = models.ForeignKey(company , on_delete=models.CASCADE, related_name='sdwe')
    builty_no = models.CharField(max_length=50)
    DC_date = models.DateField(auto_now_add=False, default=datetime.now)
    truck_details = models.ForeignKey(truck_details , on_delete=models.CASCADE, related_name='sdsdsc')
    truck_owner = models.ForeignKey(truck_owner , on_delete=models.CASCADE, related_name='cxcdfdfvd')
    consignor = models.ForeignKey(consignor , on_delete=models.CASCADE, related_name='wdsfgv')
    petrol_pump = models.ForeignKey(petrol_pump , null = True, blank = True, on_delete=models.CASCADE, related_name='wdsfgv')
    station_from = models.ForeignKey(from_station , on_delete=models.CASCADE, related_name='sdsdsdssdsdsdcs')
    station_to = models.ForeignKey(station , on_delete=models.CASCADE, related_name='dvccxcred')
    consignee = models.CharField(max_length=50)
    taluka = models.ForeignKey(taluka, on_delete=models.CASCADE, related_name='sdscsc')
    district = models.ForeignKey(district, on_delete=models.CASCADE, related_name='sddcxfw')
    onaccount = models.ForeignKey(onaccount , on_delete=models.CASCADE, related_name='wfdfgfdgv')
    article = models.ForeignKey(article , on_delete=models.CASCADE, related_name='dffdcxvc')
    bags = models.IntegerField()
    delivery_no = models.IntegerField(null = True, blank = True)
    mobile_no = models.FloatField(null = True, blank = True)
    ex_for = models.CharField(max_length=50, choices=ex_for, default="for")
    mode = models.CharField(max_length=50, choices=mode, default="cash")
    note = models.CharField(null = True, blank = True, max_length=50)
    rate = models.FloatField(default=0.0)
    mt = models.FloatField(default=0.0)
    freight = models.FloatField(default=0.0)
    less_advance = models.FloatField(default=0.0)
    less_tds = models.FloatField(null = True, blank = True, default=0.0)
    balance = models.FloatField(default=0)
    diesel = models.FloatField(default=0.0)
    editable = models.BooleanField(default=False)
    deleted = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voucher_payment_status = models.BooleanField(default=False)
    voucher_payment_mode = models.CharField(max_length=50, choices=mode1, default="cash")
    voucher_payment_bank_ac_no = models.IntegerField(default = 0, null = True, blank = True)
    voucher_payment_bank_ac_ifsc = models.IntegerField(default = 0, null = True, blank = True)
    

    def __str__(self):
        return self.builty_no

   

class ack(models.Model):

    builty = models.ForeignKey(builty, on_delete=models.CASCADE, related_name='have_ack')
    challan_number = models.CharField(max_length=50)
    challan_date = models.DateField(blank = True, null = True, auto_now_add=False)

    def __str__(self):
        return self.builty.builty_no
    
    
from django.utils import timezone

# Create an aware datetime object in Indian Standard Time
ist_datetime = timezone.localtime(timezone.now())


class ack_history(models.Model):

    builty = models.ForeignKey(builty, on_delete=models.CASCADE, related_name='have_ack3434')
    challan_number_before = models.CharField(max_length=50)
    challan_date_before = models.DateField(blank = True, null = True, auto_now_add=False)
    update_date = models.DateField(default = ist_datetime, blank=True, null=True)

    def __str__(self):
        return self.builty.builty_no

class request_edit(models.Model):

    builty = models.ForeignKey(builty, on_delete=models.CASCADE, related_name="has_request")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    history = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
   

   
