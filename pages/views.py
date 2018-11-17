from django.shortcuts import render

from .models import AboutPage

def home(request):
    context = {}
    return render(request, 'index.html', context)

def about_page(request):
    object = AboutPage.objects.all().first()
    context = {'object': object}
    return render(request, 'pages/about.html', context)