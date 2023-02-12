from django import forms

from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime


class company_Form(forms.ModelForm):
    class Meta:
        model = company
        fields = ['company_name']
        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            
        }



class consignor_Form(forms.ModelForm):
    class Meta:
        model = consignor
        fields = '__all__'
        widgets = {
            'company': forms.Select(attrs={
                'class': 'form-control', 'id': 'company'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            
           
     
            
        }

class onaccount_Form(forms.ModelForm):
    class Meta:
        model = onaccount
        fields = '__all__'
        widgets = {
            'company': forms.Select(attrs={
                'class': 'form-control', 'id': 'company'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            
            
        }

class district_Form(forms.ModelForm):
    class Meta:
        model = district
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            
            
        }

class taluka_Form(forms.ModelForm):
    class Meta:
        model = taluka
        fields = '__all__'
        widgets = {
            'district': forms.Select(attrs={
                'class': 'form-control', 'id': 'district'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            
            
        }

class station_Form(forms.ModelForm):
    class Meta:
        model = station
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            
            
        }




class article_Form(forms.ModelForm):
    class Meta:
        model = article
        fields = '__all__'
        widgets = {
            'company_name': forms.Select(attrs={
                'class': 'form-control', 'id': 'company'
            }),
            'consignor': forms.Select(attrs={
                'class': 'form-control', 'id': 'consignor'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
           
            
        }




class truck_details_Form(forms.ModelForm):
    class Meta:
        model = truck_details
        fields = '__all__'
        widgets = {
            'company': forms.Select(attrs={
                'class': 'form-control', 'id': 'company'
            }),
            'truck_owner': forms.Select(attrs={
                'class': 'form-control', 'id': 'truck_owner'
            }),
            'truck_number': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'company'
            }),
            'insurance_number': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'company'
            }),
            'permit_number': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'company'
            }),
            'puc_number': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'company'
            }),
            'fitness': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'company'
            }),
        }
           

class truck_owner_Form(forms.ModelForm):
    class Meta:
        model = truck_owner
        fields = '__all__'
        widgets = {
           
            'owner_name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'company'
            }),
            'bank_acc': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'company'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'company'
            }),
            'mobile_number': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'mobile_number'
            }),
            

        }
           