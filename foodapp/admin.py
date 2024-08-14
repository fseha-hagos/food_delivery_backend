from django.contrib import admin
from foodapp.models import User,Payment,Review,Order,Menu,Catagory,Order_items,Delivery_staff, Delivery

# Register your models here.

# class UserAdmin(admin.ModelAdmin):
#     list_display = ['username', 'email','first_name','last_name','phone_no']
#     def __str__(self):
#         return self.username

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'payment_date' ,'amount','payment_method']
    def __str__(self):
        return self.order_id
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['catagory_name']
    list_display_links = ['catagory_name']
    def __str__(self):
        return self.catagory_name
class DeliveryAdmin(admin.ModelAdmin):
    list_editable = ['delivery_status']
    list_display = ['order_id', 'staff_id' ,'delivery_status', 'delivery_time']
    def __str__(self):
        return self.delivery_status
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'rating','review_date']
    def __str__(self):
        return self.user_id
class OrderAdmin(admin.ModelAdmin):
    list_editable = ['order_status']
    list_display = ['user_id', 'order_date' ,'delivery_address','total_ammount','order_status']
class MenuAdmin(admin.ModelAdmin):
    list_editable = ['catagory_id','item_name','price','availability']
    list_display = ['catagory_id', 'item_name','price','availability']
    list_display_links = None
    def __str__(self):
        return self.item_name
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['menu_id', 'order_id' ,'quantity','price']
    def __str__(self):
        return self.menu_id
class DeliveryStaffAdmin(admin.ModelAdmin):
    list_display = ['staff_name', 'contact_number']
    list_editable = ['staff_name','contact_number']
    list_display_links = None
    def __str__(self):
        return self.staff_name

# admin.site.register(User, UserAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Catagory, CatagoryAdmin)
admin.site.register(Order_items, OrderItemsAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Delivery_staff, DeliveryStaffAdmin)



