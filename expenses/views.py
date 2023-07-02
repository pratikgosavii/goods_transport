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



    context = {
        
        'truck_count': truck_count,
        'builty_count': builty_count,
        'user_count': user_count,
        'form' : builty_Form(request.user),

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



