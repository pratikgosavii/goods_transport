from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from transactions.models import *


from store.models import *
from users.models import *

from transactions.filters import *


from django.db.models.functions import Substr

from django.core.paginator import Paginator, EmptyPage

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required(login_url='login')
def dashboard(request):

    
    builty_count = builty.objects.all().count()
    truck_count = truck_details.objects.all().count()
    user_count = User.objects.all().count()

    if request.user.is_superuser:
        builty_data = builty.objects.all().order_by('-id')
    else:
        builty_data = None


    builty_filters = builty_filter(request.GET, queryset=builty_data)
    
    data = builty_filters.qs

    page = request.GET.get('page', 1)
    paginator = Paginator(data, 20)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
   
    context = {
        
        'data': builty_data,
        'data' : builty_filters.qs,
        'builty_filter' : builty_filters,
        'truck_count': truck_count,
        'builty_count': builty_count,
        'user_count': user_count,
        'user_count': user_count,
    }
    return render(request, 'dashboard.html', context)
