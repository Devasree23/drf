from django.db import models


# Create your models here.

from django.contrib.auth.models import User

class Meal(models.Model):

    name = models.CharField(max_length=200)

    calorie= models.IntegerField()

    MEAL_CHOICES = (
            ('breakfast', 'breakfast'),
            ('lunch', 'lunch'),
            ('dinner', 'dinner'),
            ('snack', 'snack'),
           
        )
    
    mealtype = models.CharField(max_length=100,choices=MEAL_CHOICES,default="lunch")

    created_at = models.DateField(auto_now_add=True)

    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        
        return self.name