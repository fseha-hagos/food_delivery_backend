from rest_framework import serializers
from foodapp.models import Food

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'