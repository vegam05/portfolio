from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/templates/home.html')
