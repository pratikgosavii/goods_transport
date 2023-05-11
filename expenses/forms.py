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



class truck_expense_Form(forms.ModelForm):
    class Meta:
        model = truck_expense
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'taluka': forms.Select(attrs={
                'class': 'form-control sele', 'id': 'sfgfsddsf'
            }),
            
            
        }

