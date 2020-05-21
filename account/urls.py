'''
Created on May 19, 2020

@author: shamim
'''
from django.urls.conf import path
from account import views



urlpatterns = [
    path('login/', views.loginuser, name='login'),
   path('logout/',views.logoutuser, name='logout'),
   path('',views.index, name='home'),
] 