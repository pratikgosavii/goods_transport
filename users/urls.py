from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register-user/', resgister_user, name='resgister_user'),
    path('update-user/<user_id>', update_user, name='update_user'),
    path('list-user/', list_user, name='list_user'),
    path('delete-user/<user_id>', delete_user, name='delete_user'),
    path('logout/', logout_page, name='logout'),
]
