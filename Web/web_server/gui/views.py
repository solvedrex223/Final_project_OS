from django.shortcuts import render,redirect
from gui.models import User
from django.views.decorators.csrf import csrf_exempt
from file_system.FileSystem.Packages.interface import *
# Create your views here.
from django.http import HttpResponse,HttpRequest,JsonResponse
from django.views.generic.edit import CreateView
import sys
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
          new_user = User.objects.get(user = request.POST['user'])
          json = {
              'check' : 0,
          }
          return JsonResponse(json)
      except:
          new_user = User(user = request.POST['user'],password = request.POST['password'])
          new_user.save()
          lexo(["","cd", "home"],'admin',None)
          lexo(["","mkdir",request.POST['user']],'admin',None)
          lexo(["","cd",".."],'admin',None)
          json = {
              'check' : 1,
          }
          return JsonResponse(json)
    else:
        try:
            new_user = User.objects.get(user = request.GET['user'],password = request.GET['password'])
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
    return render(request,'Inicio.html')

def new_user(request):
    print(sys.path[0])
    return render(request,'new_user.html')


@csrf_exempt
def check_command (request):
    global user
    dire = ""
    if request.method == 'POST':
        if request.POST['command'] == '1':
            if user != "admin":
                lexo(["","cd","home"],user,None)
                info = lexo(["","cd",user],user,None)
                dire = user + ":~/" + info[0] + "$ "
                length = len(dire)
            else:
                dire = user + ":~/$ "
                length = len(dire)
            data = {
                'data' : dire,
                'len' : length,                               
            }
            return JsonResponse(data)
        elif request.POST['command'] == '2':
            tokens = request.POST['command2'].split()
            print (type(request.POST['data']))
            info = lexo(tokens,user,request.POST['data'])
            dire = user + ":~/" + info[0] + "$ "
            length = len(dire)
            data = {
                'data' : dire,
                'len' : length,
            }
            return JsonResponse(data)
        else:
            tokens = request.POST['command'].split()
            if tokens[1] == "mkfile":
                data = {
                    'data' : 2
                }
                return JsonResponse(data)
            else:    
                info = lexo(tokens,user,None)
                if len(info) == 1:
                    dire = user + ":~/" + info[0] + "$ "
                    length = len(dire)
                    data = {
                    'data' : dire,
                    'len' : length,
                    }
                    return JsonResponse(data)
                else:
                    dire = user + ":~/" + info[1] + "$ "
                    length = len(dire)
                    data = {
                        'data' : info[0] + dire,
                        'len' : length,
                    }
                    return JsonResponse(data)
    else:
        data = {
            'data' : " ",
        }
        return JsonResponse(data)
    
def log_out(response):
    global user
    check = lexo(['log_out'],'admin',True)
    user = ' '
    if check [0]:
        return redirect('/')
    else:
        return redirect('/')
