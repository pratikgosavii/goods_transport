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

    return date1


from django.contrib.auth.decorators import user_passes_test


from .decorators import *

from store.forms import *

@user_is_active
def add_transaction(request):

    

    if request.method == 'POST':

        forms = builty_Form(request.user, request.POST)
        DC_date = request.POST.get('DC_date')
        consignor_value = request.POST.get('consignor')


        if DC_date:

            date_time = numOfDays(DC_date)
        else:
            date_time = datetime.now(IST)
        updated_request = request.POST.copy()

        consignor_instance = consignor.objects.get(id = consignor_value)
        builty_code = consignor_instance.builty_code

        consignor_builty_count = builty.objects.filter(consignor = consignor_value).count()
        builty_code = builty_code + '-' + str(consignor_builty_count + 1)

        if request.user.is_superuser:

            user_id = request.POST.get('user')
            user_instance = User.objects.get(id = user_id)

            updated_request.update({'DC_date': date_time, 'builty_no' : builty_code, 'company' : user_instance.company})
        
        else:

            updated_request.update({'DC_date': date_time, 'builty_no' : builty_code, 'company' : request.user.company, 'user' : request.user})
       
        forms = builty_Form(request.user, updated_request)
        if forms.is_valid():

            forms.save()

            return redirect('add_transaction')

        else:

            messages.error(request, 'Something went wrong')

            company_data = company.objects.all()

            from_truck_details = truck_details_Form()
            form_truck_owner = truck_owner_Form()
            from_form_station= from_station_Form(user = request.user)
            form_station= station_Form(user = request.user)
            form_taluka = taluka_Form(user = request.user)
            form_district = district_Form()
            form_onaccount = onaccount_Form()
            form_article = article_Form(user = request.user)

            total_mt_today = 0
            total_mt_today_instance = builty.objects.filter(DC_date__gte = date.today(), DC_date__lte = date.today(), user = request.user, deleted = False)
            total_mt_today = total_mt_today_instance.aggregate(Sum('mt'))['mt__sum']


            if request.user.is_superuser:

                article_data = article.objects.all()
                consignor_data = consignor.objects.all()
                onaccount_data = onaccount.objects.all()

            else:

                article_data = article.objects.filter(company_name = request.user.company, office_location = request.user.office_location)
                consignor_data = consignor.objects.filter(company = request.user.company, office_location = request.user.office_location)
                onaccount_data = onaccount.objects.filter(company = request.user.company, office_location = request.user.office_location)
            
            data = builty.objects.filter(user = request.user, deleted = False, DC_date = date.today()).order_by('-id')

            context = {
                'form': forms,
                'company_data' : company_data,
                'form_truck_details' : from_truck_details,
                'form_truck_owner' : form_truck_owner,
                'from_form_station' : from_form_station,
                'station_Form' : form_station,
                'form_onaccount' : form_onaccount,
                'form_taluka' : form_taluka,
                'form_district' : form_district,
                'form_article' : form_article,
                'article_data' : article_data,
                'consignor_data' : consignor_data,
                'onaccount_data' : onaccount_data,
                'total_mt_today' : total_mt_today,
                'data' : data,
            }
            return render(request, 'transactions/add_builty.html', context)


        

    else:

        forms = builty_Form(user = request.user)

        company_data = company.objects.all()

        from_truck_details = truck_details_Form()
        form_truck_owner = truck_owner_Form()
        from_form_station= from_station_Form(user = request.user)
        form_station= station_Form(user = request.user)
        form_taluka = taluka_Form(user = request.user)
        form_district = district_Form()
        form_onaccount = onaccount_Form()
        form_article = article_Form(user = request.user)

        total_mt_today = 0
        total_freight = 0
        total_advance = 0
        total_balance = 0
        
        data = builty.objects.filter(user = request.user, deleted = False, DC_date = date.today()).order_by('-id')
        
        for i in data:
            total_mt_today = total_mt_today + i.mt
            total_freight = total_freight + i.freight
            total_advance = total_advance + i.less_advance
            total_balance = total_balance + i.balance

        if request.user.is_superuser:

            article_data = article.objects.all()
            consignor_data = consignor.objects.all()
            onaccount_data = onaccount.objects.all()

        else:

            article_data = article.objects.filter(company_name = request.user.company, office_location = request.user.office_location)
            consignor_data = consignor.objects.filter(company = request.user.company, office_location= request.user.office_location)
            onaccount_data = onaccount.objects.filter(company = request.user.company, office_location= request.user.office_location)


        context = {
            'form': forms,
            'company_data' : company_data,
            'form_truck_details' : from_truck_details,
            'form_truck_owner' : form_truck_owner,
            'from_form_station' : from_form_station,
            'station_Form' : form_station,
            'form_onaccount' : form_onaccount,
            'form_taluka' : form_taluka,
            'form_district' : form_district,
            'form_article' : form_article,
            'article_data' : article_data,
            'consignor_data' : consignor_data,
            'onaccount_data' : onaccount_data,
            'total_mt_today' : total_mt_today,
            'total_balance' : total_balance,
            'total_advance' : total_advance,
            'total_freight' : total_freight,
            'data' : data,
        }
        return render(request, 'transactions/add_builty.html', context)


    


@user_is_active
def update_builty(request, bulity_id):

    instance = builty.objects.get(id = bulity_id)

    form_article = article_Form(user = request.user)

    if request.method == 'POST':

        forms = builty_Form(request.user, request.POST, instance = instance)
        DC_date = request.POST.get('DC_date')

        if DC_date:

            date_time = numOfDays(DC_date)
        else:
            date_time = datetime.now(IST)
       
        updated_request = request.POST.copy()

        if request.user.is_superuser:

            user_id = request.POST.get('user')
            user_instance = User.objects.get(id = user_id)

            updated_request.update({'DC_date': date_time, 'company' : user_instance.company, 'editable' : False})
        
        else:

            updated_request.update({'DC_date': date_time, 'company' : request.user.company, 'user' : request.user, 'editable' : False})
       
        forms = builty_Form(request.user, updated_request, instance = instance)
        if forms.is_valid():

            forms.save()

            return redirect('list_transaction')

        else:

            messages.error(request, 'Something went wrong')

            if request.user.is_superuser:

                article_data = article.objects.all()
                consignor_data = consignor.objects.all()
                onaccount_data = onaccount.objects.all()

            else:

                article_data = article.objects.filter(company_name = request.user.company, office_location = request.user.office_location)
                consignor_data = consignor.objects.filter(company = request.user.company, office_location = request.user.office_location)
                onaccount_data = onaccount.objects.filter(company = request.user.company, office_location = request.user.office_location)


            context = {
                'form': forms,
                'article_data' : article_data,
                'consignor_data' : consignor_data,
                'onaccount_data' : onaccount_data,
                'form_article' : form_article,

            }

            
            return render(request, 'transactions/update_builty.html', context)


    else:

        forms = builty_Form(request.user, instance = instance)
        
        company_data = company.objects.all()

        if request.user.is_superuser:

            article_data = article.objects.all()
            consignor_data = consignor.objects.all()
            onaccount_data = onaccount.objects.all()

        else:

            article_data = article.objects.filter(company_name = request.user.company, office_location = request.user.office_location)
            consignor_data = consignor.objects.filter(company = request.user.company, office_location = request.user.office_location)
            onaccount_data = onaccount.objects.filter(company = request.user.company, office_location = request.user.office_location)
        
        from_truck_details = truck_details_Form()
        form_truck_owner = truck_owner_Form()
        form_station= station_Form(user = request.user)
        form_taluka = taluka_Form(user = request.user)
        form_district = district_Form()
        form_onaccount = onaccount_Form()
        form_article = article_Form(user = request.user)

        context = {
            'form': forms,
            'form_truck_details' : from_truck_details,
            'form_truck_owner' : form_truck_owner,
            'station_Form' : form_station,
            'form_onaccount' : form_onaccount,
            'form_taluka' : form_taluka,
            'form_district' : form_district,
            'company_data' : company_data,
            'article_data' : article_data,
            'consignor_data' : consignor_data,
            'onaccount_data' : onaccount_data,
            'form_article' : form_article,
        }
        return render(request, 'transactions/update_builty.html', context)



def delete_transaction(request, builty_id):


    builty_instance = builty.objects.get(id = builty_id)
    builty_instance.deleted = True
    builty_instance.save()

    return redirect('list_transaction')


from .filters import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models.functions import Substr

from django.db.models import Sum

@user_is_active
def list_transaction(request):

  
    if request.user.is_superuser:

        queryset_data = builty.objects.filter(deleted = False).order_by('-id')
    else:

        queryset_data = builty.objects.filter(user = request.user, deleted = False).order_by('-id')

    builty_filters = builty_filter(request.user, request.GET, queryset=queryset_data)

    filter_data = builty_filters.qs

    total_freight = filter_data.aggregate(Sum('freight'))['freight__sum']
    total_advance = filter_data.aggregate(Sum('less_advance'))['less_advance__sum']
    total_mt = filter_data.aggregate(Sum('mt'))['mt__sum']
    total_balance = filter_data.filter(have_ack__isnull = True).aggregate(Sum('balance'))['balance__sum']

    if total_balance:
        total_balance = round(total_balance, 2)
    if total_freight:
        total_freight = round(total_freight, 2)
    if total_advance:
        total_advance = round(total_advance, 2)

    page = request.GET.get('page', 1)
    paginator = Paginator(filter_data, 20)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
   
   

    

    has_filter = any(field in request.GET for field in set(builty_filters.get_fields()))

    
    context = {
        'data' : data,
        'builty_filter' : builty_filters,
        'form' : builty_Form(user = request.user),
        'total_freight' : total_freight,
        'total_advance' : total_advance,
        'total_balance' : total_balance,
        'total_mt' : total_mt,
        'has_filter' : has_filter,
    }


    return render(request, 'transactions/list_builty.html', context)




@user_is_active
def add_request_edit(request, bulity_id):

    builty_instance = builty.objects.get(id = bulity_id)

    data = request_edit.objects.filter(builty = builty_instance, status = False, history = True)

    if data:

        messages.error(request, 'Edit request already in pending')
        return redirect('request_list')
        


    else:

        request_edit.objects.create(builty = builty_instance, user = request.user, history = True)

        return redirect('request_list')


@user_is_active
@user_passes_test(lambda u: u.is_superuser)
def admin_list_request_edit(request):

    data = request_edit.objects.all()

    filtered_data = request_edit_filter(request.GET, queryset=data)
    
    data = filtered_data.qs

    page = request.GET.get('page', 1)
    paginator = Paginator(data, 20)

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

    filtered_data = request_edit_filter(request.GET, queryset=data)
    
    data = filtered_data.qs

    page = request.GET.get('page', 1)
    paginator = Paginator(data, 20)

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
@user_passes_test(lambda u: u.is_superuser)

def approve_edit(request, request_id):


    request_instance = request_edit.objects.get(id = request_id)
    request_instance.status = True
    request_instance.history = True
    request_instance.save()

    builty_instance = request_instance.builty
    builty_instance.editable = True
    builty_instance.save()



    return redirect('admin_request_list')





@user_is_active
def add_subtrip(request):

    builty_instance = builty.objects.get(id = request.POST.get('builty_id')) 

    updated_request = request.POST.copy()
    updated_request.update({'builty': builty_instance})
    form = sub_trip_From(updated_request)



    if form.is_valid():
        

        form.save()

        return JsonResponse({'status': True})


    else:

        pass

    


@user_is_active
def list_ack_all(request):

    if request.user.is_superuser:
        data = builty.objects.filter(deleted=False).order_by('-id')
    else:
        data = builty.objects.filter(user=request.user, deleted=False).order_by('-id')

    builty_filters = builty_filter(request.user, request.GET, queryset=data)
    data = builty_filters.qs

    # Calculate totals using aggregation functions
    totals = data.aggregate(
        total_freight=Sum('freight'),
        total_advance=Sum('less_advance'),
        total_balance=Sum('balance'),
        total_mt=Sum('mt')
    )

    # Access totals directly from the 'totals' dictionary
    total_freight = totals['total_freight'] or 0
    total_advance = totals['total_advance'] or 0
    total_balance = totals['total_balance'] or 0
    total_mt = totals['total_mt'] or 0

    page = request.GET.get('page', 1)
    paginator = Paginator(data, 20)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    # No need to round the totals again; they are already calculated correctly.

    context = {
        'data': data,
        'value': '----- All -----',
        'builty_filter': builty_filters,
        'total_freight': total_freight,
        'total_advance': total_advance,
        'total_balance': total_balance,
        'total_mt': total_mt,
        'form': builty_Form(request.user),
    }

    return render(request, 'transactions/list_ack_all.html', context)

@user_is_active
def list_ack(request):

    if request.user.is_superuser:
        data = ack.objects.filter(builty__deleted=False).order_by(Substr('builty__builty_no', 5))
    else:
        data = ack.objects.filter(builty__deleted=False, builty__user=request.user).order_by(Substr('builty__builty_no', 5))

    builty_filters = ack_filter(request.GET, queryset=data)
    data = builty_filters.qs

    total_freight = data.aggregate(total_freight=Sum('builty__freight'))['total_freight'] or 0
    total_advance = data.aggregate(total_advance=Sum('builty__less_advance'))['total_advance'] or 0
    total_mt = data.aggregate(total_mt=Sum('builty__mt'))['total_mt'] or 0

    page = request.GET.get('page', 1)
    paginator = Paginator(data, 20)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    total_balance = 0  # You can calculate total_balance separately if needed.

    # No need to round the totals again; they are already calculated correctly.

    context = {
        'data': data,
        'value': 'Acknowledge',
        'builty_filter': builty_filters,
        'total_freight': total_freight,
        'total_advance': total_advance,
        'total_balance': total_balance,  # Calculate this separately if needed.
        'total_mt': total_mt,
        'form': builty_Form(request.user),
    }



    return render(request, 'transactions/list_ack.html', context)

from django.db.models import Sum, F

@user_is_active
def list_not_ack(request):

    if request.user.is_superuser:
        data = builty.objects.filter(deleted=False).order_by('-id')
    else:
        data = builty.objects.filter(user=request.user, deleted=False).order_by('-id')

    builty_filters = builty_filter(request.user, request.GET, queryset=data)
    data = builty_filters.qs

    # Calculate totals using aggregation functions
    total_freight = data.aggregate(total_freight=Sum('freight'))['total_freight'] or 0
    total_advance = data.aggregate(total_advance=Sum('less_advance'))['total_advance'] or 0
    total_mt = data.aggregate(total_mt=Sum('mt'))['total_mt'] or 0

    # Calculate total_balance for builty objects without related ack objects
    total_balance = data.filter(have_ack=None).aggregate(total_balance=Sum('balance'))['total_balance'] or 0

    page = request.GET.get('page', 1)
    paginator = Paginator(data, 20)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    # No need to round the totals again; they are already calculated correctly.

    context = {
        'data': data,
        'value': 'Not Acknowledge',
        'builty_filter': builty_filters,
        'total_freight': total_freight,
        'total_advance': total_advance,
        'total_balance': total_balance,
        'total_mt': total_mt,
        'form': builty_Form(request.user),
    }



    return render(request, 'transactions/list_not_ack.html', context)


@user_is_active
def update_ack(request, challan_id):

    instance = ack.objects.get(id = challan_id).order_by('builty__builty_no')

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

            context = {

                'form' : form
            }
            return render(request, 'transactions/update_ack.html', context)


    else:

        form = builty_Form(request.user, instance=instance2)
        form2 = ack_Form(instance=instance)

        context = {

            'form' : form,
            'form2' : form2
        }

        return render(request, 'transactions/update_ack.html', context)


from datetime import date


@user_is_active
def add_ack(request):

    date_time =date.today()

    updated_request = request.POST.copy()
    updated_request.update({'challan_date': date_time})



    form = ack_Form(updated_request)



    if form.is_valid():
        

        form.save()

        return JsonResponse({'status': True})


    else:

        pass

    




@user_is_active
def mass_edit_request(request):

    builty_id = request.POST.getlist('builty_id[]')

    for i in builty_id:

        builty_instance = builty.objects.get(id = i).order_by('-id')
        request_edit.objects.create(builty = builty_instance, user = request.user, history = True)
    return JsonResponse({'status' : 'done'})

@user_is_active
def mass_approve_request(request):

    request_id = request.POST.getlist('request_id[]')

    for i in request_id:

        request_instance = request_edit.objects.get(id = i)
        request_instance.status = True
        request_instance.save()

        
    return JsonResponse({'status' : 'done'})

@user_is_active
def demo(request):

    from_station11 = from_station.objects.all()

    for from_statio in from_station11:
            # Check if the FromStation is referenced by AnotherModel
        che = builty.objects.filter(station_from=from_statio)
        if  che:
            # If it's not referenced, delete the FromStation
            
            pass
        
        else:

            from_statio.delete()

            



from django.core import serializers

@user_is_active
def get_district(request):

    taluka_id = request.POST.get('taluka_id')

    taluka_instance = taluka.objects.get(id = taluka_id)

    instance = district.objects.get(taluka = taluka_instance)

    
    data = serializers.serialize('json', [instance])

    return JsonResponse({'data' : data})
        

@user_is_active
def get_owner(request):

    truck_id = request.POST.get('truck_id')

    truck_instance = truck_details.objects.get(id = truck_id)

    instance = truck_instance.truck_owner

    
    data = serializers.serialize('json', [instance])

   

    return JsonResponse({'data' : data})
        


@user_is_active
def get_taluka_district(request):

    station_id = request.POST.get('station_id')

    station_instance = station.objects.get(id = station_id)

    instance = station_instance.taluka

    
    data = serializers.serialize('json', [instance])

    
   

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
    file_path = os.path.join(BASE_DIR) + 'bill.pdf'
    
    with open(file_path, 'wb') as pdf:
        pisa.pisaDocument(BytesIO(html.encode("UTF-8")), pdf)
        return file_path

       
def GeneratePdf(request, builty_id):

    data = builty.objects.get(id = builty_id)
    params = {
        'data': data,
    }
    file = render_to_file('transactions/generate_bill.html', params)





    
    with open(file, 'rb') as fh:
        
        return HttpResponse(fh, content_type='application/pdf')

       
def GeneratePdf_akola(request, builty_id):

    data = builty.objects.get(id = builty_id)
    params = {
        'data': data,
    }
    file = render_to_file('transactions/generate_bill_akola.html', params)





    
    with open(file, 'rb') as fh:
        
        return HttpResponse(fh, content_type='application/pdf')




def download(request):
    # fill these variables with real values

    if request.method == 'POST':

        fl_path =  request.POST.get('link')


        if os.path.exists(fl_path):

            with open(fl_path, 'r' ) as fh:
                mime_type  = mimetypes.guess_type(fl_path)
                response = HttpResponse(fh.read(), content_type=mime_type)
                response['Content-Disposition'] = 'attachment;filename=' + str(fl_path)

                return response



        else:
            messages.error(request, 'path does not exist')







import csv


def truck_report(request):


    if request.user.is_superuser:
        data = builty.objects.filter(deleted = False).order_by('id')
    else:
        data = builty.objects.filter(user = request.user, deleted = False).order_by('id')

    builty_filters = builty_filter(request.user, request.GET, queryset=data)
    
    data = builty_filters.qs

    total_mt = data.aggregate(Sum('mt'))['mt__sum']

    # date_from = request.GET.get('DC_date_start__date')
    # date_to = request.GET.get('DC_date_end__date')

    
   
    # params = {
    #     'data': data,
    #     'total_mt': total_mt,
    #     'date_today' : date.today(),
    #     'date_from' : date_from,
    #     'date_to' : date_to
    # }
    
    # file = render_to_file('transactions/dispatch_report_pdf.html', params)


    # with open(file, 'rb') as fh:
        
    #     return HttpResponse(fh, content_type='application/pdf')




    builty_filters_data1 = list(builty_filters.qs.values_list('builty_no', 'DC_date', 'truck_details__truck_number', 'truck_owner__owner_name', 'have_ack__challan_number', 'have_ack__challan_date', 'station_to__name', 'mt', 'rate', 'freight', 'less_advance', 'balance'))
    builty_filters_data = list(map(list, builty_filters_data1))
    

    vals = []
        
    vals1 = []

    total_mt = 0
    total_freight = 0
    total_advance = 0
    total_balance = 0


        
    vals.append([''])
    vals.append(['Dispatch REPORT'])
    vals.append([''])
    vals.append([''])


    
    vals1.append("Sr No")
    vals1.append("Builty No")
    vals1.append("Builty Date")
    vals1.append("Truck No")
    vals1.append("Truck Owner")
    vals1.append("Challan No")
    vals1.append("Challan Date")
    vals1.append("To")
    vals1.append("MT")
    vals1.append("Rate")
    vals1.append("Freight")
    vals1.append("Advance")
    vals1.append("Balance")
    vals.append(vals1)

    counteer = 1


    for i in builty_filters_data:
        vals1 = []
        vals1.append(counteer)
        counteer = counteer + 1
        vals1.append(i[0])
        vals1.append('%s/%s/%s' % (i[1].month, i[1].day, i[1].year))
        vals1.append(i[2])
        vals1.append(i[3])
        vals1.append(i[4])
        if i[5]:
            vals1.append('%s/%s/%s' % (i[5].month, i[5].day, i[5].year))
        else:
            vals1.append("None")

        vals1.append(i[6])
        vals1.append(i[7])
        vals1.append(i[8])
        vals1.append(i[9])
        vals1.append(i[10])
        vals1.append(i[11])
        vals.append(vals1)


        total_mt = total_mt + i[7]
        total_freight = total_freight + i[9]
        total_advance = total_advance + i[10]
        total_balance = total_balance + i[11]

    vals.append('')
    vals.append(['total', '','','','','','',total_mt,'', total_freight,total_advance, total_balance])
        
    
    name = "Report.csv"
    path = os.path.join(BASE_DIR, 'static', 'csv', name)

    with open(path, 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(vals)

    link = os.path.join(BASE_DIR, 'static', 'csv', name)

    mime_type = mimetypes.guess_type(link)[0]
    with open(path, 'rb') as f:
        response = HttpResponse(f.read(), content_type=mime_type)
        response['Content-Disposition'] = 'attachment;filename=' + name
        return response


def truck_report_list(request):


    if request.user.is_superuser:
        data = builty.objects.filter(deleted = False).order_by('id')
    else:
        data = builty.objects.filter(user = request.user, deleted = False).order_by('id')


    builty_filters = builty_filter(request.user, request.GET, queryset=data)
  
    data = builty_filters.qs

    
    total_freight = 0
    total_advance = 0
    total_balance = 0
    total_mt = 0

   

    total_freight = data.aggregate(Sum('freight'))['freight__sum']
    total_advance = data.aggregate(Sum('less_advance'))['less_advance__sum']
    total_mt = data.aggregate(Sum('mt'))['mt__sum']
    total_balance = data.filter(have_ack__isnull = True).aggregate(Sum('balance'))['balance__sum']


    page = request.GET.get('page', 1)
    paginator = Paginator(data, 20)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
   

    if total_balance:
        total_balance = round(total_balance, 2)
    if total_freight:
        total_freight = round(total_freight, 2)
    if total_advance:
        total_advance = round(total_advance, 2)
    if total_mt:
        total_mt = round(total_mt, 2)




    context = {
        'builty_filter' : builty_filters,
        'link' : None,
        'form' : builty_Form(request.user),
        'data' : data,
        'total_balance' : total_balance,
        'total_advance' : total_advance,
        'total_freight' : total_freight,
        'total_mt' : total_mt,
        'builty_filter' : builty_filters,
    }

    return render(request, 'report/truck_report.html', context)


def diesel_report(request):


    if request.user.is_superuser:
        data = builty.objects.filter(deleted = False).order_by('-id')
    else:
        data = builty.objects.filter(user = request.user, deleted = False).order_by('-id')


    builty_filters = builty_filter(request.user, request.GET, queryset=data)
    builty_filters_data1 = list(builty_filters.qs.values_list('builty_no', 'DC_date', 'truck_details__truck_number', 'station_from__name', 'station_to__name', 'consignor__name', 'onaccount__name', 'diesel', 'petrol_pump__name'))
    builty_filters_data = list(map(list, builty_filters_data1))
    

    vals = []
        
    vals1 = []

    
    vals.append([''])
    vals.append(['DIESEL REPORT'])
    vals.append([''])
    vals.append([''])
    
    vals1.append("Sr No")
    vals1.append("Builty No")
    vals1.append("Date")
    vals1.append("Truck No")
    vals1.append("Station From")
    vals1.append("Station To")
    vals1.append("Consignor")
    vals1.append("Onaccount")
    vals1.append("Diesel")
    vals1.append("Petrol Pump")
    vals.append(vals1)

    counteer = 1

    for i in builty_filters_data:
        vals1 = []
        vals1.append(counteer)
        counteer = counteer + 1
        vals1.append(i[0])
        vals1.append(i[1])
        vals1.append(i[2])
        vals1.append(i[3])
        vals1.append(i[4])
        vals1.append(i[5])
        vals1.append(i[6])
        vals1.append(i[7])
        vals1.append(i[8])
        vals.append(vals1)



    name = "Diesel_Report.csv"
    path = os.path.join(BASE_DIR) + '\static\csv\\' + name

    
    with open(path,  'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(vals)


        link = os.path.join(BASE_DIR) + '\static\csv\\' + name

    with open(path,  'r', newline="") as f:
        mime_type  = mimetypes.guess_type(link)

        response = HttpResponse(f.read(), content_type=mime_type)
        response['Content-Disposition'] = 'attachment;filename=' + str(link)

        return response


    link = os.path.join(BASE_DIR) + '\static\csv\\' + name


    
    page = request.GET.get('page', 1)
    paginator = Paginator(data, 20)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
   


    context = {
        'builty_filter' : builty_filters,
        'link' : link,
        'data' : data,
        'builty_filter' : builty_filters,
        'form' : builty_Form(request.user),
    }

    return render(request, 'report/diesel_report.html', context)

def diesel_report_list(request):


    if request.user.is_superuser:
        data = builty.objects.filter(deleted = False).order_by('-id')
    else:
        data = builty.objects.filter(user = request.user, deleted = False).order_by('-id')


    builty_filters = builty_filter(request.user, request.GET, queryset=data)
    
    data = builty_filters.qs
    
    total_diesel = 0
    
    for i in data:
        total_diesel = total_diesel + i.diesel



    page = request.GET.get('page', 1)
    paginator = Paginator(data, 20)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
   


    context = {
        'builty_filter' : builty_filters,
        'link' : None,
        'data' : data,
        'total_diesel' : total_diesel,
        'builty_filter' : builty_filters,
        'form' : builty_Form(request.user),
    }

    return render(request, 'report/diesel_report.html', context)



from django.db.models import Q

def porch_report(request):

    if request.user.is_superuser:


        data = builty.objects.filter(~Q(have_ack__challan_number = None), deleted = False).order_by('id')
    else:

        data = builty.objects.filter(~Q(have_ack__challan_number = None), user = request.user, deleted = False).order_by('id')

    builty_filters = builty_filter(request.user, request.GET, queryset=data)
    builty_filters_data1 = list(builty_filters.qs.values_list('builty_no', 'DC_date', 'have_ack__challan_number', 'have_ack__challan_date', 'truck_details__truck_number', 'station_to__name', 'mt', 'rate', 'freight', 'less_advance', 'balance'))
    builty_filters_data = list(map(list, builty_filters_data1))
    

    vals = []
        
    vals1 = []

    total_mt = 0
    total_freight = 0
    total_advance = 0
    total_balance = 0


        
    vals.append([''])
    vals.append(['PORCH REPORT'])
    vals.append([''])
    vals.append([''])


    
    vals1.append("Sr No")
    vals1.append("Builty No")
    vals1.append("Builty Date")
    vals1.append("Challan No")
    vals1.append("Challan Date")
    vals1.append("Truck No")
    vals1.append("To")
    vals1.append("MT")
    vals1.append("Rate")
    vals1.append("Freight")
    vals1.append("Advance")
    vals1.append("Balance")
    vals.append(vals1)

    counteer = 1


    for i in builty_filters_data:
        vals1 = []
        vals1.append(counteer)
        counteer = counteer + 1
        vals1.append(i[0])
        vals1.append(i[1])
        vals1.append(i[2])
        vals1.append('%s/%s/%s' % (i[3].month, i[3].day, i[3].year))
        vals1.append(i[4])
        vals1.append(i[5])
        vals1.append(i[6])
        vals1.append(i[7])
        vals1.append(i[8])
        vals1.append(i[9])
        vals1.append(i[10])
        vals.append(vals1)


        total_mt = total_mt + i[6]
        total_freight = total_freight + i[8]
        total_advance = total_advance + i[9]
        total_balance = total_balance + i[10]

    vals.append('')
    vals.append(['total', '','','','','','',total_mt,'', total_freight,total_advance, total_balance])
        
    
    name = "Report.csv"
    path = os.path.join(BASE_DIR) + '\static\csv\\' + name
    with open(path,  'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(vals)


        link = os.path.join(BASE_DIR) + '\static\csv\\' + name


    with open(path,  'r', newline="") as f:
     
        mime_type  = mimetypes.guess_type(link)

        response = HttpResponse(f.read(), content_type=mime_type)
        response['Content-Disposition'] = 'attachment;filename=' + str(link)

        return response



def porch_report_list(request):

    if request.user.is_superuser:


        data = builty.objects.filter(~Q(have_ack__challan_number = None), deleted = False).order_by('-id')
    else:

        data = builty.objects.filter(~Q(have_ack__challan_number = None), user = request.user, deleted = False).order_by('-id')

    builty_filters = builty_filter(request.user, request.GET, queryset=data)
    
    total_diesel = 0

    data = builty_filters.qs

    
    total_freight = 0
    total_advance = 0
    total_balance = 0
    total_mt = 0

    total_freight = data.aggregate(Sum('freight'))['freight__sum']
    total_advance = data.aggregate(Sum('less_advance'))['less_advance__sum']
    total_mt = data.aggregate(Sum('mt'))['mt__sum']
    total_balance = data.aggregate(Sum('balance'))['balance__sum']


    page = request.GET.get('page', 1)
    paginator = Paginator(data, 20)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)


    context = {
        'builty_filter' : builty_filters,
        'link' : None,
        'data' : data,
        'total_diesel' : total_diesel,
        'builty_filter' : builty_filters,
        'total_freight' : total_freight,
        'total_advance' : total_advance,
        'total_balance' : total_balance,
        'total_mt' : total_mt,
        'form' : builty_Form(request.user),

    }

    return render(request, 'report/porch_report.html', context)

