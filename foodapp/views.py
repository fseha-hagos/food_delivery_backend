from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from foodapp.serializer import FoodSerializer
from foodapp.models import Food
from foodapp.models import Menu
from foodapp.serializer import MenuSerializer

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

