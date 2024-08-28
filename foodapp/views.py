from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from foodapp.serializer import FoodSerializer, MenuSerializer, CatagorySerializer, DeliveryStaffSerializer, OrderSerializer, OrderItemsSerializer, DeliverySerializer, PaymentSerializer, ReviewSerializer
from foodapp.models import Food, Menu, Catagory, Delivery_staff, Order, Order_items, Delivery, Payment, Review


@csrf_exempt
def foodApi(request,id=0):
    if request.method=='GET':
        food = Food.objects.all()
        food_serializer=FoodSerializer(food,many=True)
        return JsonResponse(food_serializer.data,safe=False)
    elif request.method=='POST':
        food_data=JSONParser().parse(request)
        food_serializer=FoodSerializer(data=food_data)
        if food_serializer.is_valid():
            food_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        food_data=JSONParser().parse(request)
        food=Food.objects.get(id=id)
        food_serializer=FoodSerializer(food,data=food_data)
        if food_serializer.is_valid():
            food_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        food=Food.objects.get(id=id)
        food.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    


@csrf_exempt
def menuApi(request,id=0):
    if request.method=='GET':
        menu = Menu.objects.all()
        menu_serializer=MenuSerializer(menu,many=True)
        return JsonResponse(menu_serializer.data,safe=False)
    elif request.method=='POST':
        menu_data=JSONParser().parse(request)
        menu_serializer=MenuSerializer(data=menu_data)
        if menu_serializer.is_valid():
            menu_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        menu_data=JSONParser().parse(request)
        menu=Menu.objects.get(id=id)
        menu_serializer=MenuSerializer(menu,data=menu_data)
        if menu_serializer.is_valid():
            menu_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        menu=Menu.objects.get(id=id)
        menu.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    


@csrf_exempt
def catagoryApi(request,id=0):
    if request.method=='GET':
        catagory = Catagory.objects.all()
        catagory_serializer=CatagorySerializer(catagory,many=True)
        return JsonResponse(catagory_serializer.data,safe=False)

@csrf_exempt
def delivaryStaffApi(request,id=0):
    if request.method=='GET':
        delivery_staff = Delivery_staff.objects.all()
        delivery_staff_serializer=DeliveryStaffSerializer(delivery_staff,many=True)
        return JsonResponse(delivery_staff_serializer.data,safe=False)
    elif request.method=='POST':
        delivery_staff_data=JSONParser().parse(request)
        delivery_staff_serializer=DeliveryStaffSerializer(data=delivery_staff_data)
        if delivery_staff_serializer.is_valid():
            delivery_staff_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        delivery_staff_data=JSONParser().parse(request)
        delivery_staff=Delivery_staff.objects.get(id=id)
        delivery_staff_serializer=DeliveryStaffSerializer(delivery_staff,data=delivery_staff_data)
        if delivery_staff_serializer.is_valid():
            delivery_staff_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        delivery_staff=Delivery_staff.objects.get(id=id)
        delivery_staff.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    


@csrf_exempt
def orderApi(request,id=0):
    if request.method=='GET':
        order = Order.objects.all()
        order_serializer=OrderSerializer(order,many=True)
        return JsonResponse(order_serializer.data,safe=False)
    elif request.method=='POST':
        order_data=JSONParser().parse(request)
        order_serializer=OrderSerializer(data=order_data)
        if order_serializer.is_valid():
            saved = order_serializer.save()
            return JsonResponse(order_serializer.data,safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        order_data=JSONParser().parse(request)
        order=Order.objects.get(id=id)
        order_serializer=OrderSerializer(order,data=order_data)
        if order_serializer.is_valid():
            order_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        order=Order.objects.get(id=id)
        order.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    


@csrf_exempt
def orderItemsApi(request,id=0):
    if request.method=='GET':
        order_items = Order_items.objects.all()
        order_items_serializer=OrderItemsSerializer(order_items,many=True)
        return JsonResponse(order_items_serializer.data,safe=False)
    elif request.method=='POST':
        order_items_data=JSONParser().parse(request)
        order_items_serializer=OrderItemsSerializer(data=order_items_data)
        if order_items_serializer.is_valid():
            order_items_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        order_items_data=JSONParser().parse(request)
        order_items=Order_items.objects.get(id=id)
        order_items_serializer=OrderItemsSerializer(order_items,data=order_items_data)
        if order_items_serializer.is_valid():
            order_items_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        order_items=Order_items.objects.get(id=id)
        order_items.delete()
        return JsonResponse("Deleted Successfully",safe=False)



@csrf_exempt
def deliveryApi(request,id=0):
    if request.method=='GET':
        delivery = Delivery.objects.all()
        delivery_serializer=DeliverySerializer(delivery,many=True)
        return JsonResponse(delivery_serializer.data,safe=False)
    elif request.method=='POST':
        delivery_data=JSONParser().parse(request)
        delivery_serializer=DeliverySerializer(data=delivery_data)
        if delivery_serializer.is_valid():
            delivery_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        delivery_data=JSONParser().parse(request)
        delivery=Delivery.objects.get(id=id)
        delivery_serializer=DeliverySerializer(delivery,data=delivery_data)
        if delivery_serializer.is_valid():
            delivery_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        delivery=Delivery.objects.get(id=id)
        delivery.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    

@csrf_exempt
def reviewApi(request,id=0):
    if request.method=='GET':
        review = Review.objects.all()
        review_serializer=ReviewSerializer(review,many=True)
        return JsonResponse(review_serializer.data,safe=False)
    elif request.method=='POST':
        review_data=JSONParser().parse(request)
        review_serializer=ReviewSerializer(data=review_data)
        if review_serializer.is_valid():
            review_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        review_data=JSONParser().parse(request)
        review=Review.objects.get(id=id)
        review_serializer=ReviewSerializer(review,data=review_data)
        if review_serializer.is_valid():
            review_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        review=Review.objects.get(id=id)
        review.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    

@csrf_exempt
def paymentApi(request,id=0):
    if request.method=='GET':
        payment = Payment.objects.all()
        payment_serializer=PaymentSerializer(payment,many=True)
        return JsonResponse(payment_serializer.data,safe=False)
    elif request.method=='POST':
        payment_data=JSONParser().parse(request)
        payment_serializer=PaymentSerializer(data=payment_data)
        if payment_serializer.is_valid():
            payment_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        payment_data=JSONParser().parse(request)
        payment=Payment.objects.get(id=id)
        payment_serializer=PaymentSerializer(payment,data=payment_data)
        if payment_serializer.is_valid():
            payment_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        payment=Payment.objects.get(id=id)
        payment.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    
