from django.contrib import admin
from customer.models import Customer, FixedProduct, YardProduct, Payment

# Register your models here.
admin.site.register(Customer)
admin.site.register(FixedProduct)
admin.site.register(YardProduct)
admin.site.register(Payment)
