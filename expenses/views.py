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



def add_builty_expense(request):


    if request.method == 'POST':

        forms = builty_expense_Form(request.POST)

        if forms.is_valid():
            instance = forms.save(commit=False)
            instance.user = request.user  # Assign the logged-in user
            instance.save()

            amount = request.POST.get('amount')

            user_instance = request.user
            user_instance.balance = user_instance.balance - int(amount)
            user_instance.save()

            return redirect('list_builty_expense')
        else:
            context = {
                'form': forms
            }
            return render(request, 'expense/add_builty_expense.html', context)

    else:

        forms = builty_expense_Form()

        context = {
            'form': forms
        }
        return render(request, 'expense/add_builty_expense.html', context)
    
def add_builty_expense_ajax(request):


    pass

def add_builty_expense_json(request):


    if request.method == 'POST':

        forms = builty_expense_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_builty_expense')
        else:
            context = {
                'form': forms
            }
            return render(request, 'expense/add_builty_expense.html', context)

    else:

        forms = builty_expense_Form()

        context = {
            'form': forms
        }
        return render(request, 'expense/add_builty_expense.html', context)



from .filters import *

def list_builty_expense(request):
    
    
    if request.user.is_superuser:

        data = builty_expense.objects.all()

    else:

        data = builty_expense.objects.filter(user = request.user)

    builty_expense_filters = builty_expense_filter(request.GET, queryset=data)


    context = {
        'data': builty_expense_filters.qs,
        'expense_builty_filter' : builty_expense_filters,

    }

    return render(request, 'expense/list_builty_expense.html', context)


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
            instance = forms.save(commit=False)
            instance.user = request.user  # Assign the logged-in user
            instance.save()

            amount = request.POST.get('amount')
            
            user_instance = request.user
            user_instance.balance = user_instance.balance - int(amount)
            user_instance.save()

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



    
    
def list_diesel_expense(request):
    
    data = diesel_expense.objects.all()

    context = {
        'data': data
    }

    return render(request, 'expense/list_diesel_expense.html', context)



def add_transfer_fund(request):
    
    
    if request.method == 'POST':

        forms = transfer_fund_Form(request.POST)

        if forms.is_valid():
            instance = forms.save(commit=False)
            instance.user = request.user  # Assign the logged-in user
            instance.save()

            amount = request.POST.get('amount')
            transfer_to_user = request.POST.get('transfer_to_user')
            
            user_instance = request.user
            user_instance.balance = user_instance.balance - int(amount)
            user_instance.save()

            user_instance = request.user
            user_instance.balance = user_instance.balance + int(transfer_to_user)
            user_instance.save()

            return redirect('list_transfer_fund')
        else:
            context = {
                'form': forms
            }
            return render(request, 'expense/add_transfer_fund.html', context)

    else:

        forms = transfer_fund_Form()

        context = {
            'form': forms
        }
        return render(request, 'expense/add_transfer_fund.html', context)

      
    
    
def list_transfer_fund(request):
    
    data = transfer_fund.objects.all()

    context = {
        'data': data
    }

    return render(request, 'expense/list_transfer_fund.html', context)
    

def list_all_transfer_fund(request):
    
    data = transfer_fund.objects.all()

    context = {
        'data': data
    }

    return render(request, 'expense/list_all_transfer_fund.html', context)


def add_bank_expense(request):
    
    
    if request.method == 'POST':

        forms = bank_expense_Form(request.POST)

        if forms.is_valid():
            instance = forms.save(commit=False)
            instance.user = request.user  # Assign the logged-in user
            instance.save()

            amount = request.POST.get('amount')
            
            user_instance = request.user
            user_instance.balance = user_instance.balance - int(amount)
            user_instance.save()


            return redirect('list_bank_expense')
        else:
            context = {
                'form': forms
            }
            return render(request, 'expense/add_bank_expense.html', context)

    else:

        forms = bank_expense_Form()

        context = {
            'form': forms
        }
        return render(request, 'expense/add_bank_expense.html', context)

        

    
    
def list_bank_expense(request):
    
    data = bank_expense.objects.all()

    context = {
        'data': data
    }

    return render(request, 'expense/list_bank_expense.html', context)




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
            instance = forms.save(commit=False)
            instance.user = request.user  # Assign the logged-in user
            instance.save()

            amount = request.POST.get('amount')
            
            user_instance = request.user
            user_instance.balance = user_instance.balance - int(amount)
            user_instance.save()
            
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


def add_other_expense(request):
    
    
    if request.method == 'POST':

        forms = other_expense_Form(request.POST)

        if forms.is_valid():
            instance = forms.save(commit=False)
            instance.user = request.user  # Assign the logged-in user
            instance.save()
            return redirect('list_other_expense')
        else:
            context = {
                'form': forms
            }
            return render(request, 'expense/add_other_expense.html', context)

    else:

        forms = other_expense_Form()

        context = {
            'form': forms
        }
        return render(request, 'expense/add_other_expense.html', context)

        

    
    
def list_other_expense(request):
    
    data = other_expense.objects.all()

    context = {
        'data': data
    }

    return render(request, 'expense/list_other_expense.html', context)


def add_fund_admin(request):
    
    
    if request.method == 'POST':

        forms = fund_Form(request.POST)

        user_id = request.POST.get('user')
        amount = request.POST.get('amount')

        user_instance = User.objects.get(id = user_id)

        user_instance.balance = user_instance.balance + int(amount)

        user_instance.save()

        if forms.is_valid():
            forms.save()
            return redirect('list_fund')
        else:
            context = {
                'form': forms
            }
            return render(request, 'expense/add_fund.html', context)

    else:

        forms = fund_Form()

        context = {
            'form': forms
        }
        return render(request, 'expense/add_fund_admin.html', context)

        

    
    
def list_fund_admin(request):
    
    data = fund.objects.all()

    context = {
        'data': data
    }

    return render(request, 'expense/list_fund_admin.html', context)


def add_fund(request):
    
    
    if request.method == 'POST':


        amount = request.POST.get('amount')

        user_instance = request.user


        user_instance.balance = user_instance.balance + int(amount)

        user_instance.save()

        updated_request = request.POST.copy()
        updated_request.update({'user': user_instance})
        forms = fund_Form(updated_request)

        if forms.is_valid():

            


            forms.save()
            return redirect('list_fund')
        else:
            context = {
                'form': forms
            }
            return render(request, 'expense/add_fund.html', context)

    else:

        forms = fund_Form()

        context = {
            'form': forms
        }
        return render(request, 'expense/add_fund.html', context)

        

    
    
def list_fund(request):
    
    data = fund.objects.all()

    context = {
        'data': data
    }

    return render(request, 'expense/list_fund.html', context)

