from django.shortcuts import render, redirect
from home.models import *
from django.http import HttpResponse
# Create your views here.

def recipe(request):
    if request.method == "POST":
        data = request.POST
        
        recipe_name = data.get('Recipe_Name')
        recipe_desc = data.get('Recipe_Description')
        recipe_img = request.FILES.get('Recipe_Image')
        
        # print(recipe_name)
        # print(recipe_desc)
        # print(recipe_img)
        
        Recipe.objects.create(
            recepie_name = recipe_name,
            recepie_description = recipe_desc,
            recepie_image = recipe_img,
        )

        return redirect('/recipe/')

    
    queryset = Recipe.objects.all()
    context = {'recipes':queryset}
    
    return render(request, "recipeHome.html",context)

def delete_recipe(request,id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    # print(id)
    return redirect('/recipe/')

def update_recipe(request,id):

    queryset = Recipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST

        recipe_name = data.get('Recipe_Name')
        recipe_desc = data.get('Recipe_Description')
        recipe_img = request.FILES.get('Recipe_Image')

        queryset.recepie_name = recipe_name
        queryset.recepie_description = recipe_desc

        if recipe_img:
            queryset.recepie_image = recipe_img
        
        queryset.save()
        return redirect('/recipe/')

    context = {'recipe':queryset}        
    return render(request, "updateRecipe.html",context)
    
    