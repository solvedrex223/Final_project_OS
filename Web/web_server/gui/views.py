from django.shortcuts import render,redirect
from gui.models import User
from django.views.decorators.csrf import csrf_exempt
from file_system.FileSystem.Packages.interface import *
# Create your views here.
from django.http import HttpResponse,HttpRequest,JsonResponse
from django.views.generic.edit import CreateView
import nltk

user = " "
class indexCreateView(CreateView):
    template_name = "index.html"
    model = User
    fields = '__all__'

@csrf_exempt
def check_user (request):
    global user
    if request.method == 'POST':
      try:
          user = User.objects.get(user = request.POST['user'])
          json = {
              'check' : 0,
          }
          return JsonResponse(json)
      except:
          user = User(user = request.POST['user'],password = request.POST['password'])
          user.save()
          json = {
              'check' : 1,
          }
          return JsonResponse(json)
    else:
        try:
            user = User.objects.get(user = request.GET['user'],password = request.GET['password'])
            logged_user = request.GET['user']
            user = logged_user
            json = {
                'check' : 1,
            }
            return JsonResponse(json)
        except:
            json = {
                'check' : 0,
            }
            return JsonResponse (json)

def terminal (request):
    return render(request,'terminal.html')

def new_user(request):
    return render(request,'new_user.html')


@csrf_exempt
def check_command (request):
    global user
    if request.method == 'POST':
        if request.POST['command'] == '1':
            data = {
                'data' : user + ":~/$ ",
            }
            return JsonResponse(data)
        else:
            tokens = request.POST['command'].split()
            print (tokens)
            info = lexo(tokens,user)
            if len(info) == 1:
                data = {
                'data' : user + ":~/" + info[0] + "$ ",
                }
                return JsonResponse(data)
            else:
                data = {
                    'data' : info[0] + user + ":~/" + info[1] + "$ ",
                }
                return JsonResponse(data)
    else:
        data = {
            'data' : " ",
        }
        return JsonResponse(data)
    
