from django.db import models 
from django.utils import timezone
from django.contrib.auth.models import User
from classwebsite.adminapp.models import Product_table

# Create your models here.
class Order_table(models.Model):
    order_id = models.AutoField(primary_key=True)
    date_purchased = models.DateTimeField(default=timezone.now)
    product= models.ForeignKey(Product_table, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(unique=False)
    price = models.CharField(unique=False, max_length=11)
    purchased = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False, unique=False)



class Invoice_table(models.Model):    
    invoice_id =models.AutoField(primary_key=True)
    date_cashout =models.DateTimeField(default=timezone.now)
    user =models.ForeignKey(User, on_delete =models.CASCADE)
    total_price = models.CharField(unique=False, max_length=11)
    cashout =models.BooleanField(unique =False, default=False)