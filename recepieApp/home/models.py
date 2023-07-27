from django.db import models

# Create your models here.

class recepies(models.Model):
    recepie_name = models.CharField(max_length=100)
    recepie_description = models.TextField(max_length=500)
    recepie_image = models.ImageField(upload_to="recipe_images")
    
    