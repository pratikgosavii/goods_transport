from django.urls import path
from .views import *


urlpatterns = [


    path('dashboard', main_dashboard, name='main_dashboard'),
    
    path('add-expense-category/', add_expense_category, name='add_expense_category'),
    # path('update-expense-category/<expense_category_id>', update_expense_category, name='update_expense_category'),
    # path('delete-expense-category/<expense_category_id>', delete_expense_category, name='delete_expense_category'),
    path('list-expense-category/', list_expense_category, name='list_expense_category'),


]