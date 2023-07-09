from django import forms

from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from django.forms.widgets import DateTimeInput


class expense_category_Form(forms.ModelForm):
    class Meta:
        model = expense_category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            
        }

class employee_Form(forms.ModelForm):
    class Meta:
        model = employee
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'address'
            }),
             'mobile_no': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'mobile_no'
            }),
            
        }



class truck_expense_Form(forms.ModelForm):
    class Meta:
        model = truck_expense
        fields = '__all__'
        widgets = {
            'note': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'note'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'price'
            }),
            'truck': forms.Select(attrs={
                'class': 'form-control sele', 'id': 'truck'
            }),
            'expense_category': forms.Select(attrs={
                'class': 'form-control sele', 'id': 'expense_category'
            }),
            
            
        }


class salary_Form(forms.ModelForm):
    class Meta:
        model = salary
        fields = '__all__'
        widgets = {
            'note': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'note'
            }),
            'salary': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'salary'
            }),
            'employee': forms.Select(attrs={
                'class': 'form-control sele', 'id': 'employee'
            }),
           
            
            
        }

