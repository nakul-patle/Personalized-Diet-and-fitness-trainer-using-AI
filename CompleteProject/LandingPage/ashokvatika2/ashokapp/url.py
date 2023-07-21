from django.contrib import admin
from django.contrib.auth import login
from django.urls import path
from . import views
from .views import *

# from django.contrib import views 
from .views import LoginUser, Signup, index
from django.conf.urls.static import static

urlpatterns = [
    
   
    path('',index,name="home"),
    path('index.html',index,name="home"),
    path('about.html',about,name="about"),
    path('contact.html',contact,name="contact"),
    path('food.html',Food),
    path('Fitness.html',Fitness),
    # path('logout.html', LogoutUser),    
    # path('login.html',LoginUser,name='login'),
    # path('signup.html',Signup,name='signup'),
    #email 
    path(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
    path(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
]


