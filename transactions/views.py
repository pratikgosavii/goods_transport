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


from django.contrib.auth.decorators import user_passes_test


from .decorators import *

from store.forms import *

@user_is_active
def add_transaction(request):

    

    if request.method == 'POST':

        forms = builty_Form(request.POST)
        DC_date = request.POST.get('DC_date')
        consignor_value = request.POST.get('consignor')


        if DC_date:

            date_time = numOfDays(DC_date)
            print('in if')
        else:
            date_time = datetime.now(IST)
        print('-----------------------------------------------date_time')
        print(date_time)
        print('---------------------')
        updated_request = request.POST.copy()

        consignor_instance = consignor.objects.get(id = consignor_value)
        builty_code = consignor_instance.builty_code

        consignor_builty_count = builty.objects.filter(consignor = consignor_value).count()
        builty_code = builty_code + '-' + str(consignor_builty_count + 1)

        updated_request.update({'DC_date': date_time, 'builty_no' : builty_code, 'company' : request.user.company, 'user' : request.user})
        forms = builty_Form(updated_request)
        if forms.is_valid():

            forms.save()

            return redirect('list_transaction')

        else:

            print(forms.errors)
            company_data = company.objects.all()

            from_truck_details = truck_details_Form()
            form_truck_owner = truck_owner_Form()
            form_station= station_Form()
            form_taluka = taluka_Form()
            form_district = district_Form()
            form_onaccount = onaccount_Form()
            form_article = article_Form()

            if request.user.is_superuser:

                article_data = article.objects.all()
                consignor_data = consignor.objects.all()
                onaccount_data = onaccount.objects.all()

            else:

                article_data = article.objects.filter(company_name = request.user.company)
                consignor_data = consignor.objects.filter(company = request.user.company)
                onaccount_data = onaccount.objects.filter(company = request.user.company)

            context = {
                'form': forms,
                'company_data' : company_data,
                'form_truck_details' : from_truck_details,
                'form_truck_owner' : form_truck_owner,
                'station_Form' : form_station,
                'form_onaccount' : form_onaccount,
                'form_taluka' : form_taluka,
                'form_district' : form_district,
                'form_article' : form_article,
                'article_data' : article_data,
                'consignor_data' : consignor_data,
                'onaccount_data' : onaccount_data,
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

        if request.user.is_superuser:

            article_data = article.objects.all()
            consignor_data = consignor.objects.all()
            onaccount_data = onaccount.objects.all()

        else:

            article_data = article.objects.filter(company_name = request.user.company)
            consignor_data = consignor.objects.filter(company = request.user.company)
            onaccount_data = onaccount.objects.filter(company = request.user.company)

        context = {
            'form': forms,
            'company_data' : company_data,
            'form_truck_details' : from_truck_details,
            'form_truck_owner' : form_truck_owner,
            'station_Form' : form_station,
            'form_onaccount' : form_onaccount,
            'form_taluka' : form_taluka,
            'form_district' : form_district,
            'form_article' : form_article,
            'article_data' : article_data,
            'consignor_data' : consignor_data,
            'onaccount_data' : onaccount_data,
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
        updated_request.update({'DC_date': date_time, 'company' : request.user.company, 'user' : request.user, 'editable' : False})
        forms = builty_Form(updated_request, instance = instance)
        if forms.is_valid():

            forms.save()

            return redirect('list_transaction')

        else:

            if request.user.is_superuser:

                article_data = article.objects.all()
                consignor_data = consignor.objects.all()
                onaccount_data = onaccount.objects.all()

            else:

                article_data = article.objects.filter(company_name = request.user.company)
                consignor_data = consignor.objects.filter(company = request.user.company)
                onaccount_data = onaccount.objects.filter(company = request.user.company)


            context = {
                'form': forms,
                'article_data' : article_data,
                'consignor_data' : consignor_data,
                'onaccount_data' : onaccount_data,
            }

            
            return render(request, 'transactions/update_builty.html', context)


    else:

        forms = builty_Form(instance = instance)

        print('-----------------------------------')
        print('-----------------------------------')
        print('-----------------------------------')
        print(forms.instance.builty_no)

        if request.user.is_superuser:

            article_data = article.objects.all()
            consignor_data = consignor.objects.all()
            onaccount_data = onaccount.objects.all()

        else:

            article_data = article.objects.filter(company_name = request.user.company)
            consignor_data = consignor.objects.filter(company = request.user.company)
            onaccount_data = onaccount.objects.filter(company = request.user.company)


        context = {
            'form': forms,
            'article_data' : article_data,
            'consignor_data' : consignor_data,
            'onaccount_data' : onaccount_data,
        }
        return render(request, 'transactions/update_builty.html', context)



def delete_transaction(request, builty_id):


    builty_instance = builty.objects.get(id = builty_id)
    builty_instance.deleted = True
    builty_instance.save()

    return redirect('list_transaction')


from .filters import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@user_is_active
def list_transaction(request):

  
    if request.user.is_superuser:

        data = builty.objects.filter(deleted = False)
    else:

        data = builty.objects.filter(user = request.user, deleted = False)

    total1_freight = 0
    total1_advance = 0
    total1_balance = 0

    for i in data:

        if not i.have_ack.filter():


            total1_balance = total1_balance + i.balance

        total1_freight = total1_freight + i.freight
        total1_advance = total1_advance + i.less_advance


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
   
    total_freight = 0
    total_advance = 0
    total_balance = 0

    for i in data:

        if not i.have_ack.filter():
       
            total_balance = total_balance + i.balance

        total_freight = total_freight + i.freight
        total_advance = total_advance + i.less_advance

    
    context = {
        'data' : data,
        'builty_filter' : builty_filters,
        'form' : builty_Form(),
        'total_freight' : total_freight,
        'total_advance' : total_advance,
        'total_balance' : total_balance,
        'total1_freight' : total1_freight,
        'total1_advance' : total1_advance,
        'total1_balance' : total1_balance,
    }


    return render(request, 'transactions/list_builty.html', context)




@user_is_active
def add_request_edit(request, bulity_id):

    print('-----------')

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
def list_ack_all(request):

    data = builty.objects.filter(deleted = False)
    
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
    
    total_freight = 0
    total_advance = 0
    total_balance = 0

    for i in data:

        if not i.have_ack.filter():
       
            total_balance = total_balance + i.balance

        total_freight = total_freight + i.freight
        total_advance = total_advance + i.less_advance

    context = {
        'data' : builty_filters.qs,
        'value' : '----- All -----',
        'builty_filter' : builty_filters,
        'total_freight' : total_freight,
        'total_advance' : total_advance,
        'total_balance' : total_balance,

        
    }


    return render(request, 'transactions/list_ack_all.html', context)

@user_is_active
def list_ack(request):

    data = ack.objects.filter(builty__deleted = False)

    total1_freight = 0
    total1_advance = 0
    total1_balance = 0

    for i in data:

        total1_freight = total1_freight + i.builty.freight
        total1_advance = total1_advance + i.builty.less_advance
        total1_balance = total1_balance + i.builty.balance

    
    builty_filters = ack_filter(request.GET, queryset=data)
    data = builty_filters.qs

   

    page = request.GET.get('page', 1)
    paginator = Paginator(data, 50)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    
    total_freight = 0
    total_advance = 0
    total_balance = 0

    for i in data:

        total_freight = total_freight + i.builty.freight
        total_advance = total_advance + i.builty.less_advance
        total_balance = total1_balance + i.builty.balance


    
    context = {
        'data' : builty_filters.qs,
        'value' : 'Acknowlegde',
        'builty_filter' : builty_filters,
        'total_freight' : total_freight,
        'total_advance' : total_advance,
        'total_balance' : total_balance,
        'total1_freight' : total1_freight,
        'total1_advance' : total1_advance,
        'total1_balance' : total1_balance,


        
    }


    return render(request, 'transactions/list_ack.html', context)

@user_is_active
def list_not_ack(request):

    data = builty.objects.filter(deleted = False)

    builty_filters = builty_filter(request.GET, queryset=data)
    data = builty_filters.qs


    
    total1_freight = 0
    total1_advance = 0
    total1_balance = 0

    for i in data:

        if not i.have_ack.filter():
       
            total1_balance = total1_balance + i.balance

        total1_freight = total1_freight + i.freight
        total1_advance = total1_advance + i.less_advance


    page = request.GET.get('page', 1)
    paginator = Paginator(data, 50)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    
    total_freight = 0
    total_advance = 0
    total_balance = 0

    for i in data:

        if not i.have_ack.filter():
       
            total_balance = total_balance + i.balance

        total_freight = total_freight + i.freight
        total_advance = total_advance + i.less_advance

    context = {
        'data' : builty_filters.qs,
        'value' : 'Not Acknowlegde',
        'builty_filter' : builty_filters,
        'total_freight' : total_freight,
        'total_advance' : total_advance,
        'total_balance' : total_balance,
        'total1_freight' : total1_freight,
        'total1_advance' : total1_advance,
        'total1_balance' : total1_balance,



        
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

        print(form.errors)

    




@user_is_active
def mass_edit_request(request):

    builty_id = request.POST.getlist('builty_id[]')

    print(builty_id)

    for i in builty_id:

        builty_instance = builty.objects.get(id = i)
        request_edit.objects.create(builty = builty_instance, user = request.user, history = True)
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
        


@user_is_active
def get_taluka_district(request):

    station_id = request.POST.get('station_id')

    station_instance = station.objects.get(id = station_id)

    instance = station_instance.taluka

    
    data = serializers.serialize('json', [instance])

    print(data)
   

    return JsonResponse({'data' : data})
        



# from django.views.generic import View
# from django.utils import timezone
# from .models import *
# from threading import Thread, activeCount

# from io import BytesIO
# from django.http import HttpResponse
# from django.template.loader import get_template
# import xhtml2pdf.pisa as pisa
# import os
# from random import randint

import mimetypes


import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# def render_to_file(path: str, params: dict):

#     template = get_template(path)
#     html = template.render(params)
#     file_path = os.path.join(BASE_DIR) + 'bill.pdf'
    
#     with open(file_path, 'wb') as pdf:
#         pisa.pisaDocument(BytesIO(html.encode("UTF-8")), pdf)
#         return file_path

       
# def generate_bill(request, id):

#     sales = builty.objects.filter(deleted = False)
#     params = {
#         'today': 'today',
#         'sales': sales,
#         'request': request
#     }
#     file = render_to_file('transactions/generate_bill.html', params)





    
    # with open(file, 'rb') as fh:
    #     mime_type  = mimetypes.guess_type('receipt.pdf')
    #     response = HttpResponse(fh.read(), content_type=mime_type)
    #     response['Content-Disposition'] = 'attachment; filename=receipt.pdf'

    # return response




# importing the necessary libraries
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import render_to_string


# importing the necessary libraries
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  

# defining the function to convert an HTML file to a PDF file
def html_to_pdf(template_src, context_dict={}):
     template = get_template(template_src)
     html  = template.render(context_dict)
     result = BytesIO()
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     if not pdf.err:
         return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None

#Creating a class based view
class GeneratePdf(View):
   def get(self, request, builty_id, *args, **kwargs):
        
        data = builty.objects.get(id = builty_id)
        
        open('templates/temp.html', "w").write(render_to_string('transactions/generate_bill.html', {'data' : data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')




def download(request):
    # fill these variables with real values

    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')
    print('--------------downalodddd-----------------')

    if request.method == 'POST':

        fl_path =  request.POST.get('link')


        if os.path.exists(fl_path):

            with open(fl_path, 'r' ) as fh:
                mime_type  = mimetypes.guess_type(fl_path)
                print('---------donwlaod-----------')
                print(mime_type)
                response = HttpResponse(fh.read(), content_type=mime_type)
                response['Content-Disposition'] = 'attachment;filename=' + str(fl_path)

                return response



        else:
            print('sdfdsds')
            messages.error(request, 'path does not exist')







import csv


def truck_report(request):



    print('------------------------')




    data = builty.objects.filter(deleted = False).order_by("builty_no")

    total1_freight = 0
    total1_advance = 0
    total1_balance = 0
    total1_mt = 0
    
    for i in data:

        if not i.have_ack.filter():
    
            total1_balance = total1_balance + i.balance

        total1_freight = total1_freight + i.freight
        total1_advance = total1_advance + i.less_advance
        total1_mt = total1_mt + i.mt



    builty_filters = builty_filter(request.GET, queryset=data)
    builty_filters_data1 = list(builty_filters.qs.values_list('builty_no', 'DC_date', 'truck_details__truck_number', 'truck_owner__owner_name', 'station_from__name', 'station_to__name', 'district__name', 'consignor__name', 'onaccount__name', 'have_ack__challan_date', 'mt', 'rate', 'freight'))
    builty_filters_data = list(map(list, builty_filters_data1))
    

    vals = []
        
    vals1 = []
    vals1.append("Sr No")
    vals1.append("Builty No")
    vals1.append("Date")
    vals1.append("Truck No")
    vals1.append("Owner")
    vals1.append("Station From")
    vals1.append("Station To")
    vals1.append("District")
    vals1.append("Consignor")
    vals1.append("Account")
    vals1.append("Chal Date")
    vals1.append("MT")
    vals1.append("Rate")
    vals1.append("Freight")
    vals.append(vals1)

    counteer = 1

    for i in builty_filters_data:
        print(builty_filters_data)
        vals1 = []
        vals1.append(counteer)
        counteer = counteer + 1
        vals1.append(i[0])
        vals1.append([1])
        vals1.append(i[2])
        vals1.append(i[3])
        vals1.append(i[4])
        vals1.append(i[5])
        vals1.append(i[6])
        vals1.append(i[7])
        vals1.append(i[8])
        vals1.append(i[9])
        vals1.append(i[10])
        vals1.append(i[11])
        vals1.append(i[12])
        vals.append(vals1)




    total_freight = 0
    total_advance = 0
    total_balance = 0
    total_mt = 0

    for i in data:

        if not i.have_ack.filter():
    
            total_balance = total_balance + i.balance

        total_freight = total_freight + i.freight
        total_mt = total_mt + i.mt
        total_advance = total_advance + i.less_advance
        total_advance = total_advance + i.less_advance

    print('total_advance')
    print(total_advance)


    data = builty_filters.qs


        
    name = "Report.csv"
    path = os.path.join(BASE_DIR) + '\static\csv\\' + name
    with open(path,  'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(vals)


    link = os.path.join(BASE_DIR) + '\static\csv\\' + name

    context = {
        'builty_filter' : builty_filters,
        'link' : link,
        'data' : data,
        'total_balance' : total_balance,
        'total_advance' : total_advance,
        'total_freight' : total_freight,
        'total1_freight' : total1_freight,
        'total_mt' : total_mt,
        'total1_balance' : total1_balance,
        'total1_advance' : total1_advance,
        'total1_mt' : total1_mt,
        'builty_filter' : builty_filters,
    }

    return render(request, 'report/truck_report.html', context)


def diesel_report(request):



    print('------------------------')


    data = builty.objects.filter(deleted = False).order_by("builty_no")

    total1_diesel = 0


    for i in data:
        total1_diesel = total1_diesel + i.diesel

    builty_filters = builty_filter(request.GET, queryset=data)
    builty_filters_data1 = list(builty_filters.qs.values_list('builty_no', 'DC_date', 'truck_details__truck_number', 'station_from__name', 'station_to__name', 'consignor__name', 'onaccount__name', 'diesel', 'petrol_pump__name'))
    builty_filters_data = list(map(list, builty_filters_data1))
    

    vals = []
        
    vals1 = []
    
    vals1.append("Sr No")
    vals1.append("Builty No")
    vals1.append("Date")
    vals1.append("Truck No")
    vals1.append("Station From")
    vals1.append("Station To")
    vals1.append("Consignor")
    vals1.append("Account")
    vals1.append("Diesel")
    vals1.append("Petrol Pump")
    vals.append(vals1)

    counteer = 1

    for i in builty_filters_data:
        print(builty_filters_data)
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



    total_diesel = 0

    data = builty_filters.qs

    for i in data:
        total_diesel = total_diesel + i.diesel
        
    name = "Diesel_Report.csv"
    path = os.path.join(BASE_DIR) + '\static\csv\\' + name
    with open(path,  'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(vals)


    link = os.path.join(BASE_DIR) + '\static\csv\\' + name

    context = {
        'builty_filter' : builty_filters,
        'link' : link,
        'data' : data,
        'total_diesel' : total_diesel,
        'total1_diesel' : total1_diesel,
        'builty_filter' : builty_filters,
    }

    return render(request, 'report/diesel_report.html', context)



from django.db.models import Q

def porch_report(request):



    print('------------------------')


    data = builty.objects.filter(~Q(have_ack__challan_number = None), deleted = False).order_by("builty_no")

    
    total1_freight = 0
    total1_advance = 0
    total1_balance = 0

    for i in data:

        total1_balance = total1_balance + i.balance
        total1_freight = total1_freight + i.freight
        total1_advance = total1_advance + i.less_advance

    print(data.count())
    print('------------------------')

    builty_filters = builty_filter(request.GET, queryset=data)
    builty_filters_data1 = list(builty_filters.qs.values_list('builty_no', 'DC_date', 'have_ack__challan_number', 'have_ack__challan_date', 'truck_details__truck_number', 'station_to__name', 'mt', 'rate', 'freight', 'less_advance', 'balance'))
    builty_filters_data = list(map(list, builty_filters_data1))
    

    vals = []
        
    vals1 = []
    
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
        print(builty_filters_data)
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
        vals1.append(i[9])
        vals1.append(i[10])
        vals.append(vals1)



    total_diesel = 0

    data = builty_filters.qs
    
    print('------------------------')
    print(data.count())
    print('------------------------')

    
    total_freight = 0
    total_advance = 0
    total_balance = 0

    for i in data:

        total_balance = total_balance + i.balance
        total_freight = total_freight + i.freight
        total_advance = total_advance + i.less_advance

    
    name = "Diesel_Report.csv"
    path = os.path.join(BASE_DIR) + '\static\csv\\' + name
    with open(path,  'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(vals)


    link = os.path.join(BASE_DIR) + '\static\csv\\' + name

    context = {
        'builty_filter' : builty_filters,
        'link' : link,
        'data' : data,
        'total_diesel' : total_diesel,
        'builty_filter' : builty_filters,
        'total_freight' : total_freight,
        'total_advance' : total_advance,
        'total_balance' : total_balance,
        'total1_freight' : total1_freight,
        'total1_advance' : total1_advance,
        'total1_balance' : total1_balance,
    }

    return render(request, 'report/porch_report.html', context)

