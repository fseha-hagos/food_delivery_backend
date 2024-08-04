from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from foodapp.serializer import FoodSerializer
from foodapp.models import Food

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

