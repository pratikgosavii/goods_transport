from django.db import models

# Create your models here.


from store.models import *
from transactions.models import *


from django.utils import timezone

# Create an aware datetime object in Indian Standard Time


class expense_category(models.Model):

    name = models.CharField(max_length=120, unique=True)
    #address
    #mobile number

    
    def __str__(self):
        return self.name


class employee(models.Model):

    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=120, unique=False)
    mobile_no = models.FloatField()

    
    def __str__(self):
        return self.name



from datetime import date


class builty_expense(models.Model):

    builty = models.ForeignKey(builty, on_delete=models.CASCADE)
    amount = models.FloatField()
    is_advance = models.BooleanField(default=False)
    is_porch = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    # entry_date = models.DateTimeField(default = datetime.now, blank=True, null=True)
    entry_date = models.DateField(default=date.today)





    


class truck_expense(models.Model):

    truck = models.ForeignKey(truck_details, on_delete=models.CASCADE)
    amount = models.FloatField()
    note = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    entry_date = models.DateField(default=timezone.now)




    def __str__(self):
        return self.truck.truck_number

class transfer_fund(models.Model):

    transfer_to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sdfgedfd', blank=True, null=True)
    amount = models.FloatField()
    note = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    entry_date = models.DateField(default=timezone.now)

class diesel_rate(models.Model):

    amount = models.FloatField()

class diesel_expense(models.Model):

    builty = models.ForeignKey(builty, on_delete=models.CASCADE, related_name='sdfgedfd', blank=True, null=True)
    liter = models.FloatField()
    amount = models.FloatField()
    note = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    entry_date = models.DateField(default=timezone.now)

class truck_diesel_expense(models.Model):

    truck = models.ForeignKey(truck_details, on_delete=models.CASCADE, related_name='sdfgedfd', blank=True, null=True)
    liter = models.FloatField()
    amount = models.FloatField()
    note = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    entry_date = models.DateField(default=timezone.now)


class other_expense(models.Model):

    expense_category = models.ForeignKey(expense_category, on_delete=models.CASCADE)
    amount = models.FloatField()
    note = models.CharField(max_length=500)
    entry_date = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    

class salary(models.Model):

    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    salary = models.FloatField()
    note = models.CharField(max_length=500)
    salary_of_date = models.DateTimeField()
    entry_date = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    


    def __str__(self):
        return self.employee.name


class fund(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.FloatField()
    note = models.CharField(max_length=500)
    # entry_date = models.DateTimeField(default = datetime.now, blank=True, null=True)
    entry_date = models.DateField(default=date.today)
    
