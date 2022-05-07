from django.shortcuts import render
from .models import  AboutUs , Chef

def aboutus_list(request):
    about = AboutUs.objects.last()
    chef = Chef.objects.all()

    context = {
        'about' : about , 
        'chef' : chef
    }

    return render(request , 'aboutus/about.html' , context)

def chef(request):
    chef = Chef.objects.all()

    context = {
        'chef' : chef
    }

    return render(request , 'aboutus/chef.html' , context)