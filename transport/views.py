from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from transactions.models import *


from store.models import *
from users.models import *


@login_required(login_url='login')
def dashboard(request):
    
    builty_count = builty.objects.all().count()
    truck_count = truck_details.objects.all().count()
    user_count = User.objects.all().count()

    if request.user.is_superuser:
        builty_data = builty.objects.all()
    else:
        builty_data = None

    context = {
        
        'data': builty_data,
        'truck_count': truck_count,
        'builty_count': builty_count,
        'user_count': user_count,
    }
    return render(request, 'dashboard.html', context)
