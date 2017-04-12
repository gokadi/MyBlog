from django.shortcuts import render
from blog.models import Text
# from blog.text_analysis import init_backup

def handle_uploaded_file(f):
    Text.txt = f.read().decode('utf-8')


def upload_file(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['inputfile'])
        return render(request, 'blog/home.html')
    return render(request, 'blog/home.html')

def home(request):
    return render(request, "blog/home.html")#, {'Text': Text.txt})

def about(request):
    return render(request, "blog/about.html")

def contacts(request):
    return render(request, "blog/contacts.html")

def start(request):

    if not "start" in request.POST:
        Text.txt = request.POST('text')
        return render(request, "blog/home.html")#здесь вызов функции анализа
    else:
        return render(request, "blog/home.html")