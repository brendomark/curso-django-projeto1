from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("Olá, mundo!")
    return render(request,'receitas/home.html',context={'usuario':'brendo'})

def sobre(request):
    return render(request,'temp/temp.html')

def contato(request):
    return HttpResponse("contato!")
