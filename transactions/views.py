from django.shortcuts import render, redirect
from .forms import *

# Create your views here.


from django.core.paginator import Paginator, EmptyPage


from datetime import datetime

from django.http import FileResponse, HttpResponse, JsonResponse



import pytz

IST = pytz.timezone('Asia/Kolkata')

def numOfDays(date1):

    dt1 = date1.split('T')

    dt1 = dt1[0]
    
    dt1 = dt1.split('-')
    

    year = int(dt1[0])
    month = int(dt1[1])
    day = int(dt1[2])

    date1 = datetime(year,month, day, tzinfo=ist)

    print('--------------')
    print(date1)
    return date1




from .decorators import *

from store.forms import *

@user_is_active
def add_transaction(request):

    

    if request.method == 'POST':

        forms = builty_Form(request.POST)
        DC_date = request.POST.get('DC_date')


        if DC_date:

            date_time = numOfDays(DC_date)
            print('in if')
        else:
            date_time = datetime.now(IST)
        print('-----------------------------------------------date_time')
        print(date_time)
        print('---------------------')
        updated_request = request.POST.copy()
        updated_request.update({'DC_date': date_time, 'builty_no' : '2323', 'company' : request.user.company, 'user' : request.user})
        forms = builty_Form(updated_request)
        if forms.is_valid():

            forms.save()

            return redirect('list_transaction')

        else:

            print(forms.errors)
            company_data = company.objects.all()


            context = {
                'form': forms,
                'company_data' : company_data


            }
            return render(request, 'transactions/add_builty.html', context)
    

    else:

        forms = builty_Form()

        company_data = company.objects.all()

        from_truck_details = truck_details_Form()
        form_truck_owner = truck_owner_Form()
        form_station= station_Form()
        form_taluka = taluka_Form()
        form_district = district_Form()
        form_onaccount = onaccount_Form()
        form_article = article_Form()

        context = {
            'form': forms,
            'company_data' : company_data,
            'form_truck_details' : from_truck_details,
            'form_truck_owner' : form_truck_owner,
            'station_Form' : form_station,
            'form_onaccount' : form_onaccount,
            'form_taluka' : form_taluka,
            'form_district' : form_district,
            'form_article' : form_district,
        }
        return render(request, 'transactions/add_builty.html', context)


    


@user_is_active
def update_builty(request, bulity_id):

    instance = builty.objects.get(id = bulity_id)

    if request.method == 'POST':

        forms = builty_Form(request.POST, instance = instance)
        DC_date = request.POST.get('DC_date')


        if DC_date:

            date_time = numOfDays(DC_date)
            print('in if')
        else:
            date_time = datetime.now(IST)
        print('-----------------------------------------------date_time')
        print(date_time)
        print('---------------------')
        updated_request = request.POST.copy()
        updated_request.update({'DC_date': date_time, 'builty_no' : '2323', 'company' : request.user.company, 'user' : request.user, 'editable' : False})
        forms = builty_Form(updated_request, instance = instance)
        if forms.is_valid():

            forms.save()

            return redirect('list_transaction')

        else:

            print(forms.errors)

            context = {
                'form': forms
            }
            return render(request, 'transactions/update_builty.html', context)
    

    else:

        forms = builty_Form(instance = instance)

        print(forms.instance.editable)

        context = {
            'form': forms
        }
        return render(request, 'transactions/update_builty.html', context)


from .filters import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@user_is_active
def list_transaction(request):


    data = builty.objects.filter(user = request.user)
    print(data)

    builty_filters = builty_filter(request.GET, queryset=data)


    data = builty_filters.qs


   


    page = request.GET.get('page', 1)
    paginator = Paginator(data, 50)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    
    print('-------------------')
    
    total = 0

    for i in data:
        total = total + i.freight


    print(total)

    
    context = {
        'data' : data,
        'builty_filter' : builty_filters,
        'form' : builty_Form(),
        'total' : total,
    }


    print(data)


    return render(request, 'transactions/list_builty.html', context)




@user_is_active
def add_request_edit(request, bulity_id):

    print('-----------')

    builty_instance = builty.objects.get(id = bulity_id)

    data = request_edit.objects.filter(builty = builty_instance, status = False)

    if data:

        messages.error(request, 'Edit request already in pending')
        return redirect('request_list')
        


    else:

        request_edit.objects.create(builty = builty_instance, user = request.user)

        return redirect('request_list')


@user_is_active
def admin_list_request_edit(request):

    data = request_edit.objects.all()

    print(data)

    filtered_data = request_edit_filter(request.GET, queryset=data)
    
    data = filtered_data.qs

    print(data)


    page = request.GET.get('page', 1)
    paginator = Paginator(data, 50)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    context = {
        'data' : data,
        'request_edit_filter' : filtered_data,
        'form' : request_edit_Form(),
    }


    return render(request, 'transactions/admin_list_request.html', context)

def list_request_edit(request):

    data = request_edit.objects.filter(builty__user = request.user)

    print(data)

    filtered_data = request_edit_filter(request.GET, queryset=data)
    
    data = filtered_data.qs

    print(data)


    page = request.GET.get('page', 1)
    paginator = Paginator(data, 50)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    context = {
        'data' : data,
        'request_edit_filter' : filtered_data,
        'form' : request_edit_Form(),
    }


    return render(request, 'transactions/list_request.html', context)



@user_is_active
def approve_edit(request, request_id):


    request_instance = request_edit.objects.get(id = request_id)
    request_instance.status = True
    request_instance.save()

    builty_instance = request_instance.builty
    builty_instance.editable = True
    builty_instance.save()



    return redirect('request_list')





@user_is_active
def add_subtrip(request):


    print('hereeeeeeeeeeeeeee')



    builty_instance = builty.objects.get(id = request.POST.get('builty_id')) 

    updated_request = request.POST.copy()
    updated_request.update({'builty': builty_instance})
    form = sub_trip_From(updated_request)



    if form.is_valid():
        

        form.save()

        return JsonResponse({'status': True})


    else:

        print(form.errors)

    


@user_is_active
def list_ack(request):

    data = ack.objects.all()

    
    context = {
        'data' : data,
        'value' : 'Acknowlegde'

        
    }


    return render(request, 'transactions/list_ack.html', context)

@user_is_active
def list_not_ack(request):

    data = builty.objects.all()

    
    context = {
        'data' : data,
        'value' : 'Not Acknowlegde'

        
    }


    return render(request, 'transactions/list_not_ack.html', context)


@user_is_active
def update_ack(request, challan_id):

    instance = ack.objects.get(id = challan_id)

    instance2 = instance.builty

    if request.method == 'POST':


        form = ack_Form(request.POST)

        updated_request = request.POST.copy()
        updated_request.update({'builty': instance.builty})
        form = ack_Form(updated_request, instance=instance)

        if form.is_valid():

            form.save()

            return redirect('list_ack')

        else:

            print(form.errors)
            context = {

                'form' : form
            }
            return render(request, 'transactions/update_ack.html', context)


    else:

        form = builty_Form(instance=instance2)
        form2 = ack_Form(instance=instance)

        context = {

            'form' : form,
            'form2' : form2
        }

        return render(request, 'transactions/update_ack.html', context)

@user_is_active
def add_ack(request):




    form = ack_Form(request.POST)



    if form.is_valid():
        

        form.save()

        return JsonResponse({'status': True})


    else:

        print(form.errors)

    




@user_is_active
def mass_edit_request(request):

    builty_id = request.POST.getlist('builty_id[]')

    print(builty_id)

    for i in builty_id:

        builty_instance = builty.objects.get(id = i)
        request_edit.objects.create(builty = builty_instance, user = request.user)
    print('--------------------')
    return JsonResponse({'status' : 'done'})

@user_is_active
def mass_approve_request(request):

    request_id = request.POST.getlist('request_id[]')

    print(request_id)

    for i in request_id:

        request_instance = request_edit.objects.get(id = i)
        request_instance.status = True
        request_instance.save()

        
    print('--------------------')
    return JsonResponse({'status' : 'done'})

@user_is_active
def demo(request):

    return render(request, 'transactions/demo.html')


from django.core import serializers

@user_is_active
def get_district(request):

    taluka_id = request.POST.get('taluka_id')

    taluka_instance = taluka.objects.get(id = taluka_id)

    instance = district.objects.get(taluka = taluka_instance)

    
    data = serializers.serialize('json', [instance])

    print(data)
   

    return JsonResponse({'data' : data})
        

@user_is_active
def get_owner(request):

    truck_id = request.POST.get('truck_id')

    truck_instance = truck_details.objects.get(id = truck_id)

    instance = truck_instance.truck_owner

    
    data = serializers.serialize('json', [instance])

    print(data)
   

    return JsonResponse({'data' : data})
        



from django.views.generic import View
from django.utils import timezone
from .models import *
from threading import Thread, activeCount

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import os
from random import randint

import mimetypes


import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def render_to_file(path: str, params: dict):

    template = get_template(path)
    html = template.render(params)
    file_path = os.path.join(BASE_DIR) + '\static\csv\\bill.pdf'
    
    with open(file_path, 'wb') as pdf:
        pisa.pisaDocument(BytesIO(html.encode("UTF-8")), pdf)
        return file_path

       
def generate_bill(request):

    sales = builty.objects.all()
    params = {
        'today': 'today',
        'sales': sales,
        'request': request
    }
    file = render_to_file('transactions/generate_bill.html', params)





    
    with open(file, 'rb') as fh:
        mime_type  = mimetypes.guess_type('receipt.pdf')
        response = HttpResponse(fh.read(), content_type=mime_type)
        response['Content-Disposition'] = 'attachment; filename=receipt.pdf'

    return response