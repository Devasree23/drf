from rest_framework import serializers

from django.contrib.auth.models import User
from wellnessapp.models import Meal

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","password"]

        read_only_fields=["id"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)  


class   MealSerializer(serializers.ModelSerializer):
    class Meta:
        model= Meal 
        fields="__all__"

        read_only_fields=["id","owner","created_at"]        