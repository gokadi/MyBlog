from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Context, RequestContext
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from blog.models import Text
from blog.text_analysis import init_backup
import json
from celery.result import AsyncResult

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
    analyser = init_backup.Analysis(Text.txt)
    # syntax_, water_, orthograf_, inform_, total_, tonal_ = init_backup.analysis(Text.txt)
    syntax_, water_, orthograf_, inform_, total_ = analyser.analyse()
    context = RequestContext(request, {'Text': Text.txt, 'water': "%.2f" %water_, 'inform': "%.2f" %inform_,
                                       'orthograf': "%.2f" %orthograf_, 'syntax': "%.2f" %syntax_,
                                       'advert': "%.2f" %5, 'tonal':  "%.2f" %0, 'total': "%.2f" %total_})
    return render(request, "blog/home.html", context)

