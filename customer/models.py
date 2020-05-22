from django.db import models
import datetime










# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=30)
    phone=models.IntegerField(unique=True)
    total_due=models.FloatField(null=True, blank=True)
    reference=models.CharField(max_length=20,blank=True)
    
    class Meta:
        db_table='cutomer'
        ordering = ['name']
    
class FixedProduct(models.Model):
    details=models.CharField(max_length=50)
    price=models.IntegerField()
    time=models.DateField(default=datetime.date.today)
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE,null=True,blank=True)
    class Meta:
        db_table='fixedproduct'
        
class YardProduct(models.Model):
    details=models.CharField(max_length=50)
    yard=models.IntegerField()
    gira=models.IntegerField()
    per_yard_price=models.IntegerField()
    total_price=models.FloatField(null=True)
    time=models.DateField(default=datetime.date.today)
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE,null=True,blank=True)
    class Meta:
        db_table='yardproduct'
        
class Payment(models.Model):
    time=models.DateField(default=datetime.date.today)
    pay=models.IntegerField()
    class Meta:
        db_table='payment'
    
    
    
