from django.shortcuts import render


# Create your views here.
def home(request):
    #return HttpResponse("Olá, mundo!")
    return render(request,'receitas/home.html',context={'usuario':'brendo'})

