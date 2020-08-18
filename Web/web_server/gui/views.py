from django.shortcuts import render,redirect
from gui.models import User

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')

def log():
    x = block.Bloque(1)
    x.write_info("hola mundo")
    return redirect('')

def check_user (request):
    pass
