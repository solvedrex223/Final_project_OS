from django.shortcuts import render,redirect
import file_system.Bloque as block

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')

def log():
    x = block.Bloque(1)
    x.write_info("hola mundo")
    return redirect('')