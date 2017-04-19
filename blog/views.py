from django.http import JsonResponse
from django.shortcuts import render
from django.template import RequestContext
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from blog.models import Text
from blog.text_analysis import init_backup
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
            context = {}
            context.update(csrf(request))
            analyser = init_backup.Analysis(Text.txt)
            syntax_, water_, orthograf_, inform_, total_, tonal_, advert_ = analyser.analyse()
            context = RequestContext(request, {'water': "%.2f" % water_, 'inform': "%.2f" % inform_,
                                               'orthograf': "%.2f" % orthograf_, 'syntax': "%.2f" % syntax_,
                                               'advert': "%.2f" % advert_, 'tonal': "%.2f" % tonal_,
                                               'total': "%.2f" % total_})
            return render(request, "blog/table.html", context)
        else:
            return render(request, "blog/table.html")
