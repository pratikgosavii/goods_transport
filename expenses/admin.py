from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(expense_category)
admin.site.register(employee)
admin.site.register(truck_expense)
admin.site.register(builty_expense)
admin.site.register(salary)
admin.site.register(other_expense)
