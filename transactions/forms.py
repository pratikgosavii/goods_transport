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
             'user': forms.Select(attrs={
                'id': 'user',
                'class' : 'sele',

            }),
            'builty_no': forms.TextInput(attrs={
                'step': "0.01",
                'id': 'builty_no',
                'readonly':'readonly',
                'class' : 'se'
            }),
            'truck_details': forms.Select(attrs={
                'id' : 'truck_details',
                'class' : 'sele',

            }),
            'truck_owner': forms.Select(attrs={
                'id': 'truck_owner', 
                'class' : 'sele',

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
                'class' : 'se sele',
            }),
            'district': forms.Select(attrs={
                'id': 'district', 'class' : 'sele'
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
                
                'id': 'bags',
                'class' : 'cus'
            }),
            'rate': forms.NumberInput(attrs={
                'id': 'rate',
                'class' : 'cus',
                

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
                
            }),
            'less_tds': forms.NumberInput(attrs={
                'step': "0.01",
                'id': 'less_tds',
                'class' : 'cus',
                

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
                

            }),



            'DC_date': DateTimeInput(attrs={'type': 'date', 'class' : 'date_css'}, format = '%Y-%m-%d'),
            
        }

    def __init__(self, user, *args, **kwargs):
        self.user = user  
        super(builty_Form,self).__init__(*args, **kwargs)

        if not self.user.is_superuser:
            self.fields['district'].queryset = district.objects.filter(office_location = self.user.office_location)
            self.fields['taluka'].queryset = taluka.objects.filter(office_location = self.user.office_location)
            self.fields['station_from'].queryset = from_station.objects.filter(office_location = self.user.office_location)
            self.fields['station_to'].queryset = station.objects.filter(office_location = self.user.office_location)
            self.fields['onaccount'].queryset = onaccount.objects.filter(office_location = self.user.office_location)
            self.fields['consignor'].queryset = consignor.objects.filter(office_location = self.user.office_location)
            self.fields['article'].queryset = article.objects.filter(office_location = self.user.office_location)

class ack_Form(forms.ModelForm):
    class Meta:
        model = ack
        fields = '__all__'
        widgets = {
        'challan_date': DateTimeInput(attrs={'type': 'date', 'class' : 'date_css'}, format = '%Y-%m-%d'),
       }

class request_edit_Form(forms.ModelForm):
    class Meta:
        model = request_edit
        fields = '__all__'
       
