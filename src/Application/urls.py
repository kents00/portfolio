from django.urls import path
from Application.views import Menu, send_mail
from django.views.decorators.cache import cache_page
from . import views

appname='Application'

urlpatterns = [
    path('', views.Menu, name='home'),
    path('contact/', views.send_mail, name='contact')
]