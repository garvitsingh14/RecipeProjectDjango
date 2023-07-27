from django.shortcuts import render, redirect
from home.models import *
# Create your views here.
def recipe(request):
    if request.method == "POST":
        data = request.POST
        
        recipe_name = data.get('Recipe_Name')
        recipe_desc = data.get('Recipe_Description')
        recipe_img = request.FILES.get('Recipe_Image')
        
        print(recipe_name)
        print(recipe_desc)
        print(recipe_img)
        
        recepies.objects.create(
            recepie_name = recipe_name,
            recepie_description = recipe_desc,
            recepie_image =recipe_img,
        )
        return redirect("/recipe/")
        
    queryset = recepies.objects.all()
    context = {'recipe' : queryset}
    
    return render(request, "recipeHome.html",context)