from django.core.urlresolvers import reverse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, render_to_response
from django.template import Context, RequestContext
from django.template.context_processors import csrf
from django.utils import translation
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from blog.models import Text
from blog.text_analysis import init_backup
import json
from celery.result import AsyncResult
from annoying.decorators import ajax_request

def handle_uploaded_file(f):
    Text.txt = f.read().decode('utf-8')


@csrf_protect
def upload_file(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file']) # в кавычках - ключ, соответствующий файлу
        return JsonResponse({'Text': Text.txt})

@ajax_request
def home(request):
    try: # изначально поле пустое и приложение выкидывает AttributeError
        Text.txt = ""
    except AttributeError:
        Text.txt = ""
    finally:
        return render(request, "blog/home.html", {'Text': Text.txt})

@csrf_protect
def about(request):
    return render(request, "blog/about.html")


@csrf_protect
def contacts(request):
    return render(request, "blog/contacts.html")


@ajax_request
def start(request):
    if request.method == 'GET':
        if Text.txt != '':
            print('asdasda')
            context = {}
            context.update(csrf(request))
            analyser = init_backup.Analysis(Text.txt)
            # syntax_, water_, orthograf_, inform_, total_, tonal_ = init_backup.analysis(Text.txt)
            syntax_, water_, orthograf_, inform_, total_, tonal_ = analyser.analyse()
            context = RequestContext(request, {'water': "%.2f" % water_, 'inform': "%.2f" % inform_,
                                               'orthograf': "%.2f" % orthograf_, 'syntax': "%.2f" % syntax_,
                                               'advert': "%.2f" % 5, 'tonal': "%.2f" % tonal_,
                                               'total': "%.2f" % total_})
            # context = {'Text': Text.txt, 'water': "%.2f" % water_, 'inform': "%.2f" % inform_,
            #                                    'orthograf': "%.2f" % orthograf_, 'syntax': "%.2f" % syntax_,
            #                                    'advert': "%.2f" % 5, 'tonal': "%.2f" % tonal_,
            #                                    'total': "%.2f" % total_}
            # return JsonResponse(context)
            return render(request, "blog/table.html", context)
            # return HttpResponse(context, content_type="text/html")
        else:
            # return JsonResponse({'Text': Text.txt})
            return render(request, "blog/table.html")
            # return HttpResponse(content_type="text/html")
