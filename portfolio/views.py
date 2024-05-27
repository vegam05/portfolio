from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/templates/home.html')
def about_me(request):
    return render(request, 'portfolio/templates/about_me.html')