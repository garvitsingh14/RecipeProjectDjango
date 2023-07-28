from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank = True)
    recepie_name = models.CharField(max_length=100)
    recepie_description = models.TextField(max_length=500)
    recepie_image = models.ImageField(upload_to="recipe_images")
    
    