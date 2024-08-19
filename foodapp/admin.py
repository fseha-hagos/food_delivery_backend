from django.contrib import admin
from foodapp.models import Payment,Review,Order,Menu,Catagory,Order_items,Delivery_staff, Delivery

# Register your models here.

# class UserAdmin(admin.ModelAdmin):
#     list_display = ['username', 'email','first_name','last_name','phone_no']
#     def __str__(self):
#         return self.username

 
class PaymentAdmin(admin.ModelAdmin):
    readonly_fields = ['order_id', 'payment_date', 'amount','payment_method']
    list_display = ['order_id', 'payment_date' ,'amount','payment_method']

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['id','catagory_name']
    list_display_links = ['catagory_name']
   
   
class DeliveryAdmin(admin.ModelAdmin):
    readonly_fields = ['order_id', 'delivery_time']
    list_editable = ['delivery_status','staff_id']
    list_display = ['order_id', 'staff_id', 'delivery_time' ,'delivery_status']
    
    
   
class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ['user_id','rating','review_date','comment']
    list_display = ['user_id', 'rating','review_date','comment']
    
    
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['order_id', 'user_id', 'order_date' ,'delivery_address','total_ammount',]
    list_editable = ['order_status']
    list_display = ['order_id','user_id','order_date','delivery_address','total_ammount', 'order_status',]
    

class MenuAdmin(admin.ModelAdmin):
    readonly_fields = ['menu_id']
    list_display = ['id','item_name','menu_id','catagory_id','price','availability']
    list_display_links = ['item_name']

class OrderItemsAdmin(admin.ModelAdmin):
    readonly_fields = ['menu_id', 'order_id','quantity','price']
    list_display = ['menu_id', 'order_id','quantity','price']
    
class DeliveryStaffAdmin(admin.ModelAdmin):
    #list_editable = ['staff_name','contact_number']
    list_display = ['staff_name', 'contact_number']
    
    #list_display_links = 'staff_name'
    

# admin.site.register(User, UserAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Catagory, CatagoryAdmin)
admin.site.register(Order_items, OrderItemsAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Delivery_staff, DeliveryStaffAdmin)



