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
    
    is_advance = django_filters.BooleanFilter(
        widget=forms.CheckboxInput(attrs={'id': 'is_advance'})
    )
    
    is_porch = django_filters.BooleanFilter(
        widget=forms.CheckboxInput(attrs={'id': 'is_porch'})
    )


    
    user = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'user',
                'name' : 'user',
            })
    )

    
    


    entry_date_start = DateFilter(field_name="entry_date", lookup_expr='gte', widget=forms.DateInput(
            attrs={
                'id': 'datepicker1212',
                'type': 'date',
                'class' : 'form-control date_css'
            }
        ))


    entry_date_end = DateFilter(field_name="entry_date", lookup_expr='lte', widget=forms.DateInput(
            attrs={
            'id': 'datepicker1212',
            'type': 'date',
                'class' : 'form-control date_css'
            }
        ))
    
    


    class Meta:
        model = builty_expense
        fields = '__all__'
       
   


class builty_expense_filter1(django_filters.FilterSet):

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
                'id' : 'user',
                'name' : 'user',
            })
    )

    
    


    entry_date_start = DateFilter(field_name="entry_date", lookup_expr='gte', widget=forms.DateInput(
            attrs={
                'id': 'datepicker1212',
                'type': 'date',
                'class' : 'form-control date_css'
            }
        ))


    entry_date_end = DateFilter(field_name="entry_date", lookup_expr='lte', widget=forms.DateInput(
            attrs={
            'id': 'datepicker1212',
            'type': 'date',
                'class' : 'form-control date_css'
            }
        ))
    
    


    class Meta:
        model = builty_expense
        fields = '__all__'
       
   

from django_filters import DateFilter, DateFilter

class diesel_expense_filter(django_filters.FilterSet):

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

    
    
    entry_date_start = DateFilter(field_name="entry_date", lookup_expr='gte', widget=forms.DateTimeInput(
            attrs={
                'id': 'datetimepicker121212121',  # Use a different ID if needed
                'type': 'date',  # Change input type to date
                'class': 'form-control date_css'
            }
        ),
        initial=timezone.now().replace(hour=0, minute=0, second=0, microsecond=0))
    
    entry_date_end = DateFilter(field_name="entry_date", lookup_expr='lte', widget=forms.DateTimeInput(
            attrs={
                'id': 'datetimepicker1212',  # Use a different ID if needed
                'type': 'date',  # Change input type to date
                'class': 'form-control date_css'
            }
        ))





    class Meta:
        model = diesel_expense
        fields = '__all__'
       
   

class truck_diesel_expense_filter(django_filters.FilterSet):

    truck = django_filters.ModelChoiceFilter(
        queryset=truck_details.objects.all(),
       widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'truck'
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

    
    
    entry_date_start = DateFilter(field_name="entry_date", lookup_expr='gte', widget=forms.DateTimeInput(
            attrs={
                'id': 'datetimepicker121212121',  # Use a different ID if needed
                'type': 'date',  # Change input type to date
                'class': 'form-control date_css'
            }
        ),
        initial=timezone.now().replace(hour=0, minute=0, second=0, microsecond=0))
    
    entry_date_end = DateFilter(field_name="entry_date", lookup_expr='lte', widget=forms.DateTimeInput(
            attrs={
                'id': 'datetimepicker1212',  # Use a different ID if needed
                'type': 'date',  # Change input type to date
                'class': 'form-control date_css'
            }
        ))





    class Meta:
        model = diesel_expense
        fields = '__all__'
       
   

from django_filters import DateFilter, DateFilter

class truck_expense_filter(django_filters.FilterSet):

    truck = django_filters.ModelChoiceFilter(
        queryset=truck_details.objects.all(),
       widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'truck'
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

    
    
    entry_date_start = DateFilter(field_name="entry_date", lookup_expr='gte', widget=forms.DateTimeInput(
            attrs={
                'id': 'datetimepicker121212121',  # Use a different ID if needed
                'type': 'date',  # Change input type to date
                'class': 'form-control date_css'
            }
        ),
        initial=timezone.now().replace(hour=0, minute=0, second=0, microsecond=0))
    
    entry_date_end = DateFilter(field_name="entry_date", lookup_expr='lte', widget=forms.DateTimeInput(
            attrs={
                'id': 'datetimepicker1212',  # Use a different ID if needed
                'type': 'date',  # Change input type to date
                'class': 'form-control date_css'
            }
        ))





    class Meta:
        model = truck_expense
        fields = '__all__'
       
   


from django_filters import DateFilter, DateFilter

class transfer_fund_filter(django_filters.FilterSet):

    transfer_to_user = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
       widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'transfer_to_user'
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

    
    
    entry_date_start = DateFilter(field_name="entry_date", lookup_expr='gte', widget=forms.DateTimeInput(
            attrs={
                'id': 'datetimepicker121212121',  # Use a different ID if needed
                'type': 'date',  # Change input type to date
                'class': 'form-control date_css'
            }
        ),
        initial=timezone.now().replace(hour=0, minute=0, second=0, microsecond=0))
    
    entry_date_end = DateFilter(field_name="entry_date", lookup_expr='lte', widget=forms.DateTimeInput(
            attrs={
                'id': 'datetimepicker1212',  # Use a different ID if needed
                'type': 'date',  # Change input type to date
                'class': 'form-control date_css'
            }
        ))





    class Meta:
        model = transfer_fund
        fields = '__all__'
       

class transfer_fund1_filter(django_filters.FilterSet):

   
    
    entry_date_start = DateFilter(field_name="entry_date", lookup_expr='gte', widget=forms.DateTimeInput(
            attrs={
                'id': 'datetimepicker121212121',  # Use a different ID if needed
                'type': 'date',  # Change input type to date
                'class': 'form-control date_css'
            }
        ),
        initial=timezone.now().replace(hour=0, minute=0, second=0, microsecond=0))
    
    entry_date_end = DateFilter(field_name="entry_date", lookup_expr='lte', widget=forms.DateTimeInput(
            attrs={
                'id': 'datetimepicker1212',  # Use a different ID if needed
                'type': 'date',  # Change input type to date
                'class': 'form-control date_css'
            }
        ))





    class Meta:
        model = transfer_fund
        fields = ['entry_date_start', 'entry_date_end']
       
   



from django_filters import DateFilter, DateFilter

class other_expense_filter(django_filters.FilterSet):

    expense_category = django_filters.ModelChoiceFilter(
        queryset=expense_category.objects.all(),
       widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'expense_category'
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

    
    
    entry_date_start = DateFilter(field_name="entry_date", lookup_expr='gte', widget=forms.DateTimeInput(
            attrs={
                'id': 'datetimepicker121212121',  # Use a different ID if needed
                'type': 'date',  # Change input type to date
                'class': 'form-control date_css'
            }
        ),
        initial=timezone.now().replace(hour=0, minute=0, second=0, microsecond=0))
    
    entry_date_end = DateFilter(field_name="entry_date", lookup_expr='lte', widget=forms.DateTimeInput(
            attrs={
                'id': 'datetimepicker1212',  # Use a different ID if needed
                'type': 'date',  # Change input type to date
                'class': 'form-control date_css'
            }
        ))





    class Meta:
        model = other_expense
        fields = '__all__'
       
   

class fund_filter(django_filters.FilterSet):

    
    user = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'user'
            })
    )

    
    
    entry_date_start = DateFilter(field_name="entry_date", lookup_expr='gte', widget=forms.DateTimeInput(
            attrs={
                'id': 'datetimepicker121212121',  # Use a different ID if needed
                'type': 'date',  # Change input type to date
                'class': 'form-control date_css'
            }
        ),
        initial=timezone.now().replace(hour=0, minute=0, second=0, microsecond=0))
    
    entry_date_end = DateFilter(field_name="entry_date", lookup_expr='lte', widget=forms.DateTimeInput(
            attrs={
                'id': 'datetimepicker1212',  # Use a different ID if needed
                'type': 'date',  # Change input type to date
                'class': 'form-control date_css'
            }
        ))





    class Meta:
        model = fund
        fields = '__all__'

class closing_balance_filter(django_filters.FilterSet):

    
    user = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'user'
            })
    )

    
    
    date_start = DateFilter(field_name="date", lookup_expr='gte', widget=forms.DateTimeInput(
            attrs={
                'id': 'datetimepicker121212121',  # Use a different ID if needed
                'type': 'date',  # Change input type to date
                'class': 'form-control date_css'
            }
        ),
        initial=timezone.now().replace(hour=0, minute=0, second=0, microsecond=0))
    
    date_end = DateFilter(field_name="date", lookup_expr='lte', widget=forms.DateTimeInput(
            attrs={
                'id': 'datetimepicker1212',  # Use a different ID if needed
                'type': 'date',  # Change input type to date
                'class': 'form-control date_css'
            }
        ))





    class Meta:
        model = closing_balance
        fields = '__all__'
       
   


class salary_filter(django_filters.FilterSet):

    employee = django_filters.ModelChoiceFilter(
        queryset=employee.objects.all(),
       widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'employee'
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

    
    
    salary_of_date_start = DateFilter(field_name="salary_of_date", lookup_expr='gte', widget=forms.DateTimeInput(
            attrs={
                'id': 'datetimepicker121212121',  # Use a different ID if needed
                'type': 'date',  # Change input type to date
                'class': 'form-control date_css'
            }
        ),
        initial=timezone.now().replace(hour=0, minute=0, second=0, microsecond=0))
    
    salary_of_date_end = DateFilter(field_name="salary_of_date", lookup_expr='lte', widget=forms.DateTimeInput(
            attrs={
                'id': 'datetimepicker1212',  # Use a different ID if needed
                'type': 'date',  # Change input type to date
                'class': 'form-control date_css'
            }
        ))
    
    entry_date_start = DateFilter(field_name="entry_date", lookup_expr='gte', widget=forms.DateTimeInput(
            attrs={
                'id': 'datetimepicker121212121',  # Use a different ID if needed
                'type': 'date',  # Change input type to date
                'class': 'form-control date_css'
            }
        ),
        initial=timezone.now().replace(hour=0, minute=0, second=0, microsecond=0))
    
    entry_date_end = DateFilter(field_name="entry_date", lookup_expr='lte', widget=forms.DateTimeInput(
            attrs={
                'id': 'datetimepicker1212',  # Use a different ID if needed
                'type': 'date',  # Change input type to date
                'class': 'form-control date_css'
            }
        ))





    class Meta:
        model = salary
        fields = '__all__'
       
   

