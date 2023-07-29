from django.shortcuts import render, redirect
from home.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/login-page/")
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

    if request.GET.get('Search'):
        queryset = queryset.filter(recepie_name__icontains = request.GET.get('Search'))

    context = {'recipes':queryset}
    return render(request, "recipeHome.html",context)


@login_required(login_url="/login-page/")
def delete_recipe(request,id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    # print(id)
    return redirect('/recipe/')

@login_required(login_url="/login-page/")
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


def logout_page(request):
    logout(request)
    return redirect('/login-page/')
    
def login_page(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')


        if not User.objects.filter(username = username).exists():
           messages.info(request, "Invalid Username")
           return redirect('/login-page/')

        user = authenticate(username = username, password=password)

        if user is None:
            messages.info(request, "Invalid Password")
            return redirect('/login-page/')
        else:
            login(request,user)
            return redirect('/recipe/')


    return render(request, "loginPage.html")

def register_papge(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = User.objects.filter(username = username)

        if user.exists():
           messages.info(request, "Username Already Exists.")
           return redirect('/registeration-page/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )

        user.set_password(password)
        user.save()
        messages.info(request, "Account Created Successfully.")

        return redirect('/recipe/')

    return render(request, "registerationPage.html")
    