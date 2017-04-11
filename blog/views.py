from django.shortcuts import render
from django.shortcuts import render_to_response
from blog.models import Text
from blog.text_analysis import advert

def home(request):
    return render(request, "blog/home.html")

def about(request):
    return render(request, "blog/about.html")

def contacts(request):
    return render(request, "blog/contacts.html")

def start(request):

    if not "start" in request.POST:
        # Text.txt = request.POST('text')
        return render(request, "blog/about.html")#здесь вызов функции анализа
    else:
        return render(request, "blog/home.html")