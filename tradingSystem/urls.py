from django.urls import path
from django.conf.urls import include
from . import views

app_name = 'tradingSystem'

urlpatterns = [
    path('', views.goto_login, name='goto_login'),
    path('mylogin', views.mylogin, name='mylogin'),
    path('base', views.base, name='base'),
]


