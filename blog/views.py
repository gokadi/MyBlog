from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template import Context, RequestContext
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from blog.models import Text
from blog.text_analysis import init_backup


def handle_uploaded_file(f):
    Text.txt = f.read().decode('utf-8')


@csrf_protect
def upload_file(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['inputfile'])
        return render(request, 'blog/home.html', {'Text': Text.txt})
    return render(request, 'blog/home.html')


@csrf_protect
def home(request):
    Text.txt = ""
    return render(request, "blog/home.html", {'Text': Text.txt})


@csrf_protect
def about(request):
    return render(request, "blog/about.html")


@csrf_protect
def contacts(request):
    return render(request, "blog/contacts.html")


@csrf_protect
def start(request):
    context = {}
    context.update(csrf(request))
    syntax_, water_, orthograf_, inform_, total_ = init_backup.analysis(Text.txt)
    context = RequestContext(request, {'Text': Text.txt, 'water': water_, 'inform': inform_, 'orthograf': orthograf_,
                                       'syntax': syntax_, 'advert': 5, 'tonal': 6, 'total': total_})
    return render(request, "blog/home.html", context)
