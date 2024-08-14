from rest_framework import serializers
from foodapp.models import Food,Payment,User,Review,Order,Menu,Order_items,Catagory,Delivery_staff,Delivery

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_items
        fields = '__all__'

class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = '__all__'
class DeliveryStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery_staff
        fields = '__all__'
class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'