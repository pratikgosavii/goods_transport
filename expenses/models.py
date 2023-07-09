from django.db import models

# Create your models here.


from store.models import *


class expense_category(models.Model):

    name = models.CharField(max_length=120, unique=True)
    #address
    #mobile number

    
    def __str__(self):
        return self.name


class employee(models.Model):

    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=120, unique=False)
    mobile_no = models.IntegerField()

    
    def __str__(self):
        return self.name



class truck_expense(models.Model):

    truck = models.ForeignKey(truck_details, on_delete=models.CASCADE)
    expense_category = models.ForeignKey(expense_category, on_delete=models.CASCADE)
    price = models.IntegerField()
    note = models.CharField(max_length=500)
    
    def __str__(self):
        return self.truck.truck_number


class salary(models.Model):

    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    salary = models.IntegerField()
    note = models.CharField(max_length=500)
    
    def __str__(self):
        return self.employee.name

