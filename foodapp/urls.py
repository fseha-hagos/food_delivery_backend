    
from . import views
from django.urls import re_path as url


urlpatterns = [

    url(r'^food$',views.foodApi),
    url(r'^food$',views.foodApi),
    url(r'^food/([0-9]+)$',views.foodApi),

    url(r'^menu$',views.menuApi),
    url(r'^menu$',views.menuApi),
    url(r'^menu/([0-9]+)$',views.menuApi),

    url(r'^catagory$',views.catagoryApi),
    url(r'^catagory/([0-9]+)$',views.catagoryApi),

    url(r'^deliver-staff$',views.delivaryStaffApi),
    url(r'^delivery-staff$',views.delivaryStaffApi),
    url(r'^delivery-staff/([0-9]+)$',views.delivaryStaffApi),

    url(r'^order$',views.orderApi),
    url(r'^order$',views.orderApi),
    url(r'^order/([0-9]+)$',views.orderApi),

    url(r'^order-items$',views.orderItemsApi),
    url(r'^order-items$',views.orderItemsApi),
    url(r'^order-items/([0-9]+)$',views.orderItemsApi),

    url(r'^delivery$',views.deliveryApi),
    url(r'^delivery$',views.deliveryApi),
    url(r'^delivery/([0-9]+)$',views.deliveryApi),

    url(r'^payment$',views.paymentApi),
    url(r'^payment$',views.paymentApi),
    url(r'^payment/([0-9]+)$',views.paymentApi),

    url(r'^pay$',views.payApi),
    url(r'^pay$',views.payApi),
    url(r'^pay/([0-9]+)$',views.payApi),

    url(r'^review$',views.reviewApi),
    url(r'^review$',views.reviewApi),
    url(r'^review/([0-9]+)$',views.reviewApi),
]