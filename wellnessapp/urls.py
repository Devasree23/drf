from django.urls import path
from wellnessapp import views

urlpatterns=[
    path("signup/",views.UserCreateView.as_view()),
    path("meal/",views.MealListCreateView.as_view()),
    path("meal/<int:pk>/",views.MealUpdateRetrieveDestroyView.as_view()),
    path("meal/<int:pk>/calorietotal/",views.CalorieView.as_view()),

]