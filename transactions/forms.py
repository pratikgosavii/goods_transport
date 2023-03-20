from django import forms
from django.forms.widgets import DateTimeInput

from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime



class builty_Form(forms.ModelForm):
    class Meta:
        model = builty
        fields = '__all__'
        widgets = {
            'company': forms.Select(attrs={
                'id': 'company'
            }),
            'builty_no': forms.NumberInput(attrs={
                'step': "0.01",
                'id': 'builty_no',
                'readonly':'readonly'
            }),
            'truck_details': forms.Select(attrs={
                'id': 'truck_details',
                'class' : 'sele',

            }),
            'truck_owner': forms.Select(attrs={
                'id': 'truck_owner', 'class' : 'se',

            }),
            'consignor': forms.Select(attrs={
                'id': 'consignor',
                'class' : 'sele',
            }),
            'petrol_pump': forms.Select(attrs={
                'id': 'petrol_pump',
                'class' : 'sele',
            }),
            'station_from': forms.Select(attrs={
                'id': 'station_from',
                'class' : 'sele',
            }),
            'station_to': forms.Select(attrs={
                'id': 'station_to',
                'class' : 'sele',

            }),
            'taluka': forms.Select(attrs={
                'id': 'taluka',
                'class' : 'se',
            }),
            'district': forms.Select(attrs={
                'id': 'district', 'class' : 'se'
            }),
            'consignee': forms.TextInput(attrs={
                'id': 'consignee'
            }),
            'onaccount': forms.Select(attrs={
                'id': 'onaccount',
                'class' : 'sele',
            }),
             'mobile_no': forms.NumberInput(attrs={
                

            }),
            'article': forms.Select(attrs={
                'id': 'article',                
                'class' : 'sele',
            }),
            'bags': forms.NumberInput(attrs={
                'value' : 0.0,
                'id': 'bags',
                'class' : 'cus'
            }),
            'rate': forms.NumberInput(attrs={
                'id': 'rate',
                'class' : 'cus',
                'value' : 0.0

            }),

           
            'delivery_no': forms.NumberInput(attrs={
                'step': "0.01",
                'id': 'delivery_no',
                'class' : 'cus'
            }),
            'ex_for': forms.Select(attrs={
                'id': 'ex_for',
                'class' : 'cus'
            }),
            'mode': forms.Select(attrs={
                'id': 'mode',
                'class' : 'cus'
            }),
            'note': forms.TextInput(attrs={
                'id': 'note',
                'class' : 'cus'
            }),
            'mt': forms.NumberInput(attrs={
                'id': 'mt',
                'class' : 'se cus',
                'readonly':'readonly',
                'value' : 0.0

            }),
            'freight': forms.NumberInput(attrs={
                'step': "0.01",
                'id': 'freight',
                'class' : 'se cus',
                'readonly':'readonly'
            }),
            'less_advance': forms.NumberInput(attrs={
                'step': "0.01",
                'id': 'less_advance',
                'class' : 'cus',
                'value' : 0.0
            }),
            'less_tds': forms.NumberInput(attrs={
                'step': "0.01",
                'id': 'less_tds',
                'class' : 'cus',
                'value' : 0.0

            }),
            'balance': forms.NumberInput(attrs={
                'step': "0.01",
                'id': 'balance',
                'class' : 'se cus'
            }),
            'diesel': forms.NumberInput(attrs={
                'step': "0.01",
                'id': 'diesel',
                'class' : 'cus',
                'value' : 0.0

            }),



            'DC_date': DateTimeInput(attrs={'type': 'date'}, format = '%Y-%m-%d'),
            
        }




class ack_Form(forms.ModelForm):
    class Meta:
        model = ack
        fields = '__all__'
       

class request_edit_Form(forms.ModelForm):
    class Meta:
        model = request_edit
        fields = '__all__'
       

class sub_trip_From(forms.ModelForm):
    class Meta:
        model = sub_trip
        fields = '__all__'
       