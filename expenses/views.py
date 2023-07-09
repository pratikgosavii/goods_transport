from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required


from transactions.models import *
from transactions.filters import *



from django.db.models.functions import Substr

from django.core.paginator import Paginator, EmptyPage

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.shortcuts import render, redirect


from .forms import *





@login_required(login_url='login')
def main_dashboard(request):

    if request.user.is_superuser:

        builty_count = builty.objects.all().count()
    
    else:
        builty_count = builty.objects.filter(user = request.user).count()
    
    truck_count = truck_details.objects.all().count()
    user_count = User.objects.all().count()

    queryset_data = builty.objects.filter(user = request.user, deleted = False).order_by('-id')

    builty_filters = builty_filter(request.user, request.GET, queryset=queryset_data)
    
    context = {
        
        'truck_count': truck_count,
        'builty_count': builty_count,
        'user_count': user_count,
        'form' : builty_Form(request.user),
        'builty_filter' : builty_filters,


    }
    return render(request, 'expense/main_dashboard.html', context)



def add_expense_category(request):


    if request.method == 'POST':

        forms = expense_category_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_expense_category')
        else:
            context = {
                'form': forms
            }
            return render(request, 'expense/add_expense_category.html', context)

    else:

        forms = expense_category_Form()

        context = {
            'form': forms
        }
        return render(request, 'expense/add_expense_category.html', context)

        

def list_expense_category(request):
    
    data = expense_category.objects.all()

    context = {
        'data': data
    }

    return render(request, 'expense/list_expense_category.html', context)




def add_truck_expense(request):
    
    
    if request.method == 'POST':

        forms = truck_expense_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_truck_expense')
        else:
            context = {
                'form': forms
            }
            return render(request, 'expense/add_truck_expense.html', context)

    else:

        forms = truck_expense_Form()

        context = {
            'form': forms
        }
        return render(request, 'expense/add_truck_expense.html', context)

        

    
    
def list_truck_expense(request):
    
    data = truck_expense.objects.all()

    context = {
        'data': data
    }

    return render(request, 'expense/list_truck_expense.html', context)




def add_employee(request):
    
    
    if request.method == 'POST':

        forms = employee_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_employee')
        else:
            context = {
                'form': forms
            }
            return render(request, 'expense/add_employee.html', context)

    else:

        forms = employee_Form()

        context = {
            'form': forms
        }
        return render(request, 'expense/add_employee.html', context)

        

    
    
def list_employee(request):
    
    data = employee.objects.all()

    context = {
        'data': data
    }

    return render(request, 'expense/list_employee.html', context)



def add_salary(request):
    
    
    if request.method == 'POST':

        forms = salary_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_salary')
        else:
            context = {
                'form': forms
            }
            return render(request, 'expense/add_salary.html', context)

    else:

        forms = salary_Form()

        context = {
            'form': forms
        }
        return render(request, 'expense/add_salary.html', context)

        

    
    
def list_salary(request):
    
    data = salary.objects.all()

    context = {
        'data': data
    }

    return render(request, 'expense/list_salary.html', context)

