import django_filters
from django_filters import DateFilter, CharFilter
from django.forms.widgets import DateInput
from django import forms

from .models import *
from users.models import *
from .forms import *




class builty_filter(django_filters.FilterSet):

    consignor = django_filters.ModelChoiceFilter(
        queryset=consignor.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class' : 'form-control',
                'id' : 'consignor'
            })
    )

    station_from = django_filters.ModelChoiceFilter(
        queryset=from_station.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'station_from'
            })
    )
    
    article = django_filters.ModelChoiceFilter(
        queryset=article.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'article'
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

    district = django_filters.ModelChoiceFilter(
        queryset=district.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'district'
            })
    )
   
    truck_details = django_filters.ModelMultipleChoiceFilter(
        queryset=truck_details.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class' : 'form-control',
                'id' : 'truck_details'
            })
    )

    truck_owner = django_filters.ModelMultipleChoiceFilter(
        queryset=truck_owner.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class' : '',
                'id' : 'truck_owner'
            })
    )
    petrol_pump = django_filters.ModelChoiceFilter(
        queryset=petrol_pump.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'petrol_pump'
            })
    )
    builty_no = django_filters.ModelChoiceFilter(
        queryset=builty.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control date_css sele',
                'id' : 'builty_no'
            })
    )

    

    DC_date_start__date = DateFilter(field_name="DC_date", lookup_expr='gte', widget=forms.DateInput(
            attrs={
                'id': 'datepicker1212',
                'type': 'date',
                'class' : 'form-control date_css'
            }
        ))


    DC_date_end__date = DateFilter(field_name="DC_date", lookup_expr='lte', widget=forms.DateInput(
            attrs={
            'id': 'datepicker1212',
            'type': 'date',
                'class' : 'form-control date_css'
            }
        ))
    challan_date_start__date = DateFilter(field_name="have_ack__challan_date", lookup_expr='gte', widget=forms.DateInput(
            attrs={
                'id': 'datepicke3434r1212',
                'type': 'date',
                'class' : 'form-control date_css'
            }
        ))


    challan_date_end__date = DateFilter(field_name="have_ack__challan_date", lookup_expr='lte', widget=forms.DateInput(
            attrs={
            'id': 'date343234picker1212',
            'type': 'date',
                'class' : 'form-control date_css'
            }
        ))

    


    class Meta:
        model = builty
        fields = '__all__'
       
    def __init__(self, user, *args, **kwargs):
        super(builty_filter,self).__init__(*args, **kwargs)
        request = user
        if not request.is_superuser:
            self.filters['district'].queryset = district.objects.filter(office_location = request.office_location)
            self.filters['taluka'].queryset = taluka.objects.filter(office_location = request.office_location)
            self.filters['station_from'].queryset = station.objects.filter(office_location = request.office_location)
            self.filters['station_to'].queryset = station.objects.filter(office_location = request.office_location)
            self.filters['onaccount'].queryset = onaccount.objects.filter(office_location = request.office_location)
            self.filters['consignor'].queryset = consignor.objects.filter(office_location = request.office_location)
            self.filters['article'].queryset = article.objects.filter(office_location = request.office_location)
            self.filters['builty_no'].queryset = builty.objects.filter(user = request)





class ack_filter(django_filters.FilterSet):

    builty__consignor = django_filters.ModelChoiceFilter(
        queryset=consignor.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'company'
            })
    )

    builty__user = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'user'
            })
    )

    builty__article = django_filters.ModelChoiceFilter(
        queryset=article.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'company'
            })
    )

    builty__user = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'user'
            })
    )
   
    builty__truck_details = django_filters.ModelChoiceFilter(
        queryset=truck_details.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'truck_details'
            })
    )
    builty__truck_owner = django_filters.ModelChoiceFilter(
        queryset=truck_owner.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'truck_owner'
            })
    )
    builty__station_from = django_filters.ModelChoiceFilter(
        queryset=station.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'station'
            })
    )
    builty__petrol_pump = django_filters.ModelChoiceFilter(
        queryset=petrol_pump.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'petrol_pump'
            })
    )

    builty__builty_no = django_filters.ModelChoiceFilter(
        queryset=builty.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control date_css sele',
                'id' : 'builty_no'
            })
    )


    builty__DC_date_start__date = DateFilter(field_name="builty__DC_date", lookup_expr='gte', widget=forms.DateInput(
            attrs={
                'id': 'dfrrfvgfr',
                'type': 'date',
                'class' : 'form-control'
            }
        ))


    builty__DC_date_end__date = DateFilter(field_name="builty__DC_date", lookup_expr='lte', widget=forms.DateInput(
            attrs={
            'id': 'grdfvfrggt',
            'type': 'date',
                'class' : 'form-control'
            }
        ))
    challan_date_start__date = DateFilter(field_name="challan_date", lookup_expr='gte', widget=forms.DateInput(
            attrs={
                'id': 'datepickewdsddr1212',
                'type': 'date',
                'class' : 'form-control'
            }
        ))


    challan_date_end__date = DateFilter(field_name="challan_date", lookup_expr='lte', widget=forms.DateInput(
            attrs={
            'id': 'datepickedvfdcr1212',
            'type': 'date',
                'class' : 'form-control'
            }
        ))

    


    class Meta:
        model = ack
        fields = '__all__'
       
   

class request_edit_filter(django_filters.FilterSet):

    
    builty_no = django_filters.CharFilter(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control sele',
                'id' : 'builty_no'
            })
    )

    
    class Meta:
        model = request_edit
        fields = ['builty_no', 'status']
       
   