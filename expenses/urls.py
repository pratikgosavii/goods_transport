from django.urls import path
from .views import *


urlpatterns = [


    path('dashboard', main_dashboard, name='main_dashboard'),

    path('add-builty-category/', add_expense_category, name='add_expense_category'),
    # path('update-expense-category/<expense_category_id>', update_expense_category, name='update_expense_category'),
    # path('delete-expense-category/<expense_category_id>', delete_expense_category, name='delete_expense_category'),
    path('list-expense-category/', list_expense_category, name='list_expense_category'),
   
    
    # path('update-builty-expense/<builty_expense_id>', update_builty_expense, name='update_builty_expense'),
    # path('delete-builty-expense/<builty_expense_id>', delete_builty_expense, name='delete_builty_expense'),
    path('list-builty-expense/', list_builty_expense, name='list_builty_expense'),
    
   
    path('add-truck-expense/', add_truck_expense, name='add_truck_expense'),
    path('update-truck-expense/<truck_expense_id>', update_truck_expense, name='update_truck_expense'),
    path('delete-truck-expense/<truck_expense_id>', delete_truck_expense, name='delete_truck_expense'),
    path('list-truck-expense/', list_truck_expense, name='list_truck_expense'),
    
    path('list-delete/', list_delete, name='list_delete'),

    path('check-balance/', check_balance, name='check_balance'),
   
    path('add-diesel-expense/', add_diesel_expense, name='add_diesel_expense'),
    path('update-diesel-expense/<diesel_expense_id>', update_diesel_expense, name='update_diesel_expense'),
    path('delete-diesel-expense/<diesel_expense_id>', delete_diesel_expense, name='delete_diesel_expense'),
    path('list-diesel-expense/', list_diesel_expense, name='list_diesel_expense'),
    
    path('add-truck-diesel-expense/', add_truck_diesel_expense, name='add_truck_diesel_expense'),
    path('update-truck-diesel-expense/<truck_diesel_expense_id>', update_truck_diesel_expense, name='update_truck_diesel_expense'),
    path('delete-truck-diesel-expense/<truck_diesel_expense_id>', delete_truck_diesel_expense, name='delete_truck_diesel_expense'),
    path('list-truck-diesel-expense/', list_truck_diesel_expense, name='list_truck_diesel_expense'),
    
    path('add-diesel-rate/', add_diesel_rate, name='add_diesel_rate'),

    path('add-transfer-fund/', add_transfer_fund, name='add_transfer_fund'),
    path('update-transfer-fund/<transfer_fund_id>', update_transfer_fund, name='update_transfer_fund'),
    path('delete-transfer-fund/<transfer_fund_id>', delete_transfer_fund, name='delete_transfer_fund'),
    path('list-transfer-fund/', list_transfer_fund, name='list_transfer_fund'),
   
    path('add-employee/', add_employee, name='add_employee'),
    path('update-employee/<employee_id>', update_employee, name='update_employee'),
    path('delete-employee/<employee_id>', delete_employee, name='delete_employee'),
    path('list-employee/', list_employee, name='list_employee'),
   
    path('add-salary/', add_salary, name='add_salary'),
    path('update-salary/<salary_id>', update_salary, name='update_salary'),
    path('delete-salary/<salary_id>', delete_salary, name='delete_salary'),
    path('list-salary/', list_salary, name='list_salary'),
    
    path('delete-all/', list_delete, name='list_delete'),
   
    path('add-other-expense/', add_other_expense, name='add_other_expense'),
    path('update-other_expense/<other_expense_id>', update_other_expense, name='update_other_expense'),
    path('delete-other_expense/<other_expense_id>', delete_other_expense, name='delete_other_expense'),
    path('list-other-expense/', list_other_expense, name='list_other_expense'),
   

    path('add-fund/', add_fund, name='add_fund'),
    path('update-fund/<fund_id>', update_fund, name='update_fund'),
    path('delete-fund/<fund_id>', delete_fund, name='delete_fund'),
    path('list-fund/', list_fund, name='list_fund'),

    path('master-report/', master_report, name='master_report'),
    path('master-report-list/', master_report_list, name='master_report_list'),


]