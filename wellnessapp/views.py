from django.shortcuts import render,get_object_or_404
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions,serializers

from wellnessapp.models import Meal
from wellnessapp.serializers import UserCreationSerializer,MealSerializer
from wellnessapp.permission import IsOwnerPermissionRequired 
# Create your views here.

class UserCreateView(APIView):
    def post(self,request,*args,**kwargs):
        serializer_instance=UserCreationSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.data)
        

class MealListCreateView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        qs=Meal.objects.filter(owner=request.user)
        serializer_instance=MealSerializer(qs,many=True) 
        return  Response(data=serializer_instance.data)  

    def post(self,request,*args,**kwargs):
        serializer_instance=MealSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(owner=request.user)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)    
        

class MealUpdateRetrieveDestroyView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[IsOwnerPermissionRequired] 

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        meal_instance=get_object_or_404(Meal,id=id)
        
       
        serializer_instance=MealSerializer(meal_instance)
        self.check_object_permissions(request,meal_instance)
        return Response(data=serializer_instance.data)
    
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        meal_instance=get_object_or_404(Meal,id=id)
        
        meal_instance.delete()
        self.check_object_permissions(request,meal_instance)
        return Response(data={"message":"deleted"})
    
    def put(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        meal_instance = get_object_or_404(Meal, id=id)

       
        serializer_instance = MealSerializer(instance=meal_instance, data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        
        return Response(data=serializer_instance.errors)
    

class CalorieView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):  
        calorie_total=Meal.objects.filter(owner=request.user).values("calorie").aggregate(total=Sum("calorie"))
        return Response(data=calorie_total)


           
