from django.urls import path
from .views import *


urlpatterns = [


    path('dashboard', main_dashboard, name='main_dashboard'),
    
    path('add-expense-category/', add_expense_category, name='add_expense_category'),
    # path('update-expense-category/<expense_category_id>', update_expense_category, name='update_expense_category'),
    # path('delete-expense-category/<expense_category_id>', delete_expense_category, name='delete_expense_category'),
    path('list-expense-category/', list_expense_category, name='list_expense_category'),
   
    path('add-truck-expense/', add_truck_expense, name='add_truck_expense'),
    # path('update-truck-expense/<truck_expense_id>', update_truck_expense, name='update_truck_expense'),
    # path('delete-truck-expense/<truck_expense_id>', delete_truck_expense, name='delete_truck_expense'),
    path('list-truck-expense/', list_truck_expense, name='list_truck_expense'),
   
    path('add-employee/', add_employee, name='add_employee'),
    # path('update-employee/<employee_id>', update_employee, name='update_employee'),
    # path('delete-employee/<employee_id>', delete_employee, name='delete_employee'),
    path('list-employee/', list_employee, name='list_employee'),
   
    path('add-salary/', add_salary, name='add_salary'),
    # path('update-salary/<salary_id>', update_salary, name='update_salary'),
    # path('delete-salary/<salary_id>', delete_salary, name='delete_salary'),
    path('list-salary/', list_salary, name='list_salary'),


]