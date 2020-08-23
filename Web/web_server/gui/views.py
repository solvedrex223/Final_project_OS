from django.shortcuts import render,redirect
from gui.models import User
from django.views.decorators.csrf import csrf_exempt
from file_system.FileSystem.Packages.interface import *
# Create your views here.
from django.http import HttpResponse,HttpRequest,JsonResponse
from django.views.generic.edit import CreateView
import nltk

class indexCreateView(CreateView):
    template_name = "index.html"
    model = User
    fields = '__all__'

def log():
    pass

def check_user (request):
    pass

def terminal (request):
    return render(request,'terminal.html')

@csrf_exempt
def check_command (request):
    if request.method == 'POST':
        tokens = nltk.word_tokenize(request.POST['command'])
        print(tokens[0])
        data = {
            'command' : tokens[0],
            'dir' : tokens[1],
        }
        return JsonResponse(data)
    else:
        data = {
            'command' : " ",
        }
        return JsonResponse(data)
    
