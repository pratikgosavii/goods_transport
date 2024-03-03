import django_filters
from django_filters import DateFilter, CharFilter
from django.forms.widgets import DateInput
from django import forms

from .models import *
from users.models import *
from .forms import *





class builty_expense_filter(django_filters.FilterSet):

    builty = django_filters.ModelChoiceFilter(
        queryset=builty.objects.all(),
       widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'builty'
            })
    )

    
    user = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'user'
            })
    )

    
    

    payment_date_start__date = DateFilter(field_name="payment_date", lookup_expr='gte', widget=forms.DateInput(
            attrs={
                'id': 'datepicker1212',
                'type': 'date',
                'class' : 'form-control date_css'
            }
        ))


    payment_date_end__date = DateFilter(field_name="payment_date", lookup_expr='lte', widget=forms.DateInput(
            attrs={
            'id': 'datepicker1212',
            'type': 'date',
                'class' : 'form-control date_css'
            }
        ))



    expense_date_start__date = DateFilter(field_name="expense_date", lookup_expr='gte', widget=forms.DateInput(
            attrs={
                'id': 'datepicker1212',
                'type': 'date',
                'class' : 'form-control date_css'
            }
        ))


    expense_date_end__date = DateFilter(field_name="expense_date", lookup_expr='lte', widget=forms.DateInput(
            attrs={
            'id': 'datepicker1212',
            'type': 'date',
                'class' : 'form-control date_css'
            }
        ))
    
    entry_date_start__date = DateFilter(field_name="entry_date", lookup_expr='gte', widget=forms.DateInput(
            attrs={
                'id': 'datepicker1212',
                'type': 'date',
                'class' : 'form-control date_css'
            }
        ))


    entry_date_end__date = DateFilter(field_name="entry_date", lookup_expr='lte', widget=forms.DateInput(
            attrs={
            'id': 'datepicker1212',
            'type': 'date',
                'class' : 'form-control date_css'
            }
        ))
    
    


    class Meta:
        model = builty_expense
        fields = '__all__'
       
   

