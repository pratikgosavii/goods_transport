from django.urls import path

from .views import *
from store import views

urlpatterns = [

   
    path('add-transaction/', add_transaction, name='add_transaction'),
    path('update-transaction/<bulity_id>', update_builty, name='update_builty'),
    path('delete-transaction/<builty_id>', delete_transaction, name='delete_transaction'),
    path('list-transaction/', list_transaction, name='list_transaction'),

    path('request-edit-builty/<bulity_id>', add_request_edit, name='request_edit'),
    
    path('save_financial_year/', save_financial_year, name='save_financial_year'),
    
    path('admin-request-list', admin_list_request_edit, name='admin_request_list'),
    path('request-list', list_request_edit, name='request_list'),
    path('approve-edit-builty/<request_id>', approve_edit, name='approve_edit'),


    path('copy-data', copy_date, name='copy_date'),

    path('add-ack', add_ack, name='add_ack'),

    path('fixing-data', fixing_data, name='fixing_data'),

    path('list-ack-all', list_ack_all, name='list_ack_all'),
    path('list-ack', list_ack, name='list_ack'),
    path('list-not-ack', list_not_ack, name='list_not_ack'),
    
    path('update-ack/<challan_id>', update_ack, name='update_ack'),

    
    path('mass_edit_request', mass_edit_request, name='mass_edit_request'),
    path('mass_approve_request', mass_approve_request, name='mass_approve_request'),

    path('demo', demo, name='demo'),

    path('downald-data/', downalo_data, name='downalo_data'),


    path('get_district', get_district, name='get_district'),
    path('get_owner', get_owner, name='get_owner'),
    path('get_taluka_district', get_taluka_district, name='get_taluka_district'),


    # path('generate_bill/<builty_id>', GeneratePdf, name='generate_bill'),

    # path('generate_bill-akola/<builty_id>', GeneratePdf_akola, name='generate_bill_akola'),

    path('download', download, name='download'),

    path('voucher-report', voucher_report, name='voucher_report'),
    path('voucher-report-list', voucher_report_list, name='voucher_report_list'),

    path('truck-report', truck_report, name='truck_report'),
    path('truck-report-excel', truck_report_excel, name='truck_report_excel'),
    path('truck-report-list', truck_report_list, name='truck_report_list'),
    path('diesel-report', diesel_report, name='diesel_report'),
    path('diesel-report-list', diesel_report_list, name='diesel_report_list'),
    path('porch-report', porch_report, name='porch_report'),
    path('porch-report-list', porch_report_list, name='porch_report_list'),



]
