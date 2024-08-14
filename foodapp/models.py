from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from authentication.models import User

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    fee = models.IntegerField()




# class User(models.Model):
#     username = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password =models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     phone_no = models.CharField(max_length=100)
#     user_type = models.CharField(max_length=100)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

class Delivery_staff(models.Model):
    staff_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=50)

class Order(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_address = models.CharField(max_length=200)
    total_ammount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    order_status = models.CharField(max_length=100)



class Catagory(models.Model):
    catagory_name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

class Menu(models.Model):
    catagory_id = models.ForeignKey(Catagory, on_delete=models.SET_NULL, null=True)
    item_name = models.CharField(max_length=100)
    description =models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    availability = models.BooleanField()
   
    
class Order_items(models.Model):
    
    menu_id = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)   
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE) 
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

class Delivery(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Delivery_staff, on_delete=models.SET_NULL, null=True)
    delivery_status = models.CharField(max_length=100)
    delivery_time = models.DateTimeField()

class Payment(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_method = models.CharField(max_length=100)

class Review(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField()
    comment = models.TextField(max_length=1000)
    review_date = models.DateTimeField()