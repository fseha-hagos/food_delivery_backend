from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from authentication.models import User
from django.utils import timezone
from django.contrib import admin
from django.utils.html import format_html
import random
import string
import os
import uuid

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

def delivery_staff_unique_id():
        length = 6
        while True :
            staff_id = "".join(random.choices(string.ascii_uppercase, k=length))
            if(Delivery_staff.objects.filter(staff_id = staff_id).count() == 0):
                break
        return staff_id
class Delivery_staff(models.Model):
    staff_id = models.CharField(primary_key=True, default=delivery_staff_unique_id, max_length=50, editable=False)
    staff_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=50)

    def __str__(self):
        return self.staff_name


def generate_unique_code_order():
        length = 8
        while True :
            currentTime = timezone.now
            order_id = str(random.randrange(1000000000, 9999999999))
            # order_id = str(currentTime).join(random.choices(string.ascii_uppercase, k=length))
            if(Order.objects.filter(order_id = order_id).count() == 0):
                break
        return order_id

class Order(models.Model):
    class DeliveryStatusChoice(models.TextChoices):
        status1 =  'R0', 'Pending'
        status2 =  'R1','On Delivery'
        status3 =  'R2','Delivered'
    order_id = models.CharField(primary_key=True, default=generate_unique_code_order, max_length=20)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now)
    delivery_address = models.CharField(max_length=200)
    total_ammount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    order_status = models.CharField(max_length=2, choices=DeliveryStatusChoice.choices , default=DeliveryStatusChoice.status1)
  
    
    def __str__(self):
        return str(self.order_id)
    # def order_items(self):
    #     order_items = Order_items.objects.filter(order_id = self.order_id)
    @admin.display()
    def order_items(self):
        items = Order_items.objects.filter(order_id = self.order_id)
        it= []
        for i in items :
            it.append(i) 
        #     return i
        
        return  it



class Catagory(models.Model):
    catagory_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    catagory_name = models.CharField(unique=True, max_length=100)
    description = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.catagory_name
    


def generate_unique_code():
        length = 6
        while True :
            menu_id = "".join(random.choices(string.ascii_uppercase, k=length))
            if(Menu.objects.filter(menu_id = menu_id).count() == 0):
                break
        return menu_id
def user_directory_path(instance, filename):
    # Get Current Date
    todays_date = timezone.now()

    path = "item-images/".format(todays_date.year, todays_date.month, todays_date.day)
    extension = "." + filename.split('.')[-1]
    stringId = str(uuid.uuid4())
    randInt = str(random.randint(10, 99))

    # Filename reformat
    filename_reformat = stringId + randInt + extension

    return os.path.join(path, filename_reformat)
class Menu(models.Model):
   
    menu_id = models.CharField( primary_key=True,max_length=8, default=generate_unique_code, unique=True, editable=False)
    #catagory_id = models.OneToOneField(Catagory, on_delete=models.SET_NULL, null=True)
    catagory_id = models.ForeignKey(Catagory, on_delete=models.SET_NULL, null=True)
    item_name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to=user_directory_path, default="default.jpg")
    description =models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    availability = models.BooleanField()
    
    def __str__(self):
        return self.item_name
   
    

class Order_items(models.Model):
    order_item_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    menu_id = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)   
    order_id = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True) 
    quantity = models.IntegerField(default=1, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    

    def __str__(self):
        return str(self.menu_id)

class Delivery(models.Model):
    class DeliveryStatusChoice(models.TextChoices):
        status1 =  'R0', 'Pending'
        status2 =  'R1','On Delivery'
        status3 =  'R2','Delivered'
    delivery_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Delivery_staff, on_delete=models.SET_NULL, null=True)
    delivery_status = models.CharField(max_length=2, choices=DeliveryStatusChoice.choices, default=DeliveryStatusChoice.status1)
    delivery_time = models.DateTimeField(default=timezone.now)

    def __str__ (self):
        return str(self.delivery_status)



class Payment(models.Model):
       
    payment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    payment_date = models.DateTimeField(default=timezone.now, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_method = models.CharField(max_length=100)
    payment_varified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.payment_id)

class Review(models.Model):
    review_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField()
    comment = models.TextField(max_length=1000)
    review_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.rating)