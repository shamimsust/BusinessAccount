'''
Created on May 13, 2020

@author: shamim
'''

from django.urls.conf import path
from customer import views
urlpatterns=[
    path('addcustomer/',views.addcustomer, name="addcustomer"),
    path('addfixedproduct/<int:cid>',views.addfixedproduct, name="addfixedproduct"),
    path('addyardproduct/<int:cid>',views.addyardproduct, name="addyardproduct"),
    path('show/<int:c1>',views.showcustomer, name="showcustomer"),
    path('purchasedetails/<int:c1>',views.purchasedetails, name="purchasedetails"),
    path('findcustomer/',views.findcustomer, name="findcustomer"),
    path('payment/<int:cid>',views.payment, name="payment"),
   
    ]