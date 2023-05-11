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
    builty_data = None
    builty_filters = None
    total1_freight = None
    total1_advance = None
    total1_balance = None
    total1_mt = None
    total_freight = None
    total_advance = None
    total_balance = None
    total_mt = None
    data = None

    if request.user.is_superuser:
        builty_data = builty.objects.all().order_by('-id')
        
        total1_freight = 0
        total1_advance = 0
        total1_balance = 0
        total1_mt = 0

        for i in builty_data:

            if not i.have_ack.filter():


                total1_balance = total1_balance + i.balance

            total1_freight = total1_freight + i.freight
            total1_advance = total1_advance + i.less_advance
            total1_mt = total1_mt + i.mt

        builty_filters = builty_filter(request.user, request.GET, queryset=builty_data)
        
        data = builty_filters.qs


        total_freight = 0
        total_advance = 0
        total_balance = 0
        total_mt = 0

        


        
        page = request.GET.get('page', 1)
        paginator = Paginator(data, 20)

        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
    

        for i in data:

            if not i.have_ack.filter():
        
                total_balance = total_balance + i.balance

            total_freight = total_freight + i.freight
            total_advance = total_advance + i.less_advance
            total_mt = total_mt + i.mt

        
        total_balance = round(total_balance, 2)
        total_advance = round(total_advance, 2)
        total_freight = round(total_freight, 2)
        total1_freight = round(total1_freight, 2)
        total_mt = round(total_mt, 2)
        total1_balance = round(total1_balance, 2)
        total1_advance = round(total1_advance, 2)
        total1_mt = round(total1_mt, 2)


    context = {
        
        'data': data,
        'builty_filter' : builty_filters,
        'truck_count': truck_count,
        'builty_count': builty_count,
        'user_count': user_count,
        'total_freight' : total_freight,
        'total_advance' : total_advance,
        'total_balance' : total_balance,
        'total1_freight' : total1_freight,
        'total1_advance' : total1_advance,
        'total1_balance' : total1_balance,
        'total_mt' : total_mt,
        'total1_mt' : total1_mt,
        'form' : builty_Form(request.user),

    }
    return render(request, 'main_dashboard.html', context)



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



