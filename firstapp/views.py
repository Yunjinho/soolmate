from django.shortcuts import render
import json
import requests
from .models import Beer_snack, Soju_snack, Whiskey_snack, Wine_snack, RiceWine_snack, Cocktail_snack

# Create your views here.
def index(request):
    return render(request, 'index.html')

def snacks(request):
    return render(request, 'snacks.html')

def area(request):
    return render(request, 'area.html')

def recipe(request):
    return render(request, 'recipe.html')