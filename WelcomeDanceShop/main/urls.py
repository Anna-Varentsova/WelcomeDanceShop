from django.urls import path, include
from .views import index, RegisterUser, LoginUser, logout_user, success_mail, send, process_mail

app_name = 'main'

urlpatterns = [
    path('welcome-dance-shop/contacts/process', process_mail, name='process_mail'),
    path('welcome-dance-shop/contacts/success', success_mail, name='success_mail'),
    path('welcome-dance-shop/contacts', send, name='contacts'),
    path('welcome-dance-shop/register', RegisterUser.as_view(), name='register'),
    path('welcome-dance-shop/login', LoginUser.as_view(), name='login'),
    path('welcome-dance-shop/logout', logout_user, name='logout'),
    path('welcome-dance-shop/', index, name='to_main'),
]