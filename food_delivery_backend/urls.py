"""
URL configuration for food_delivery_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from foodapp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    url('authentication/', include('authentication.urls')),
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
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
