from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def noticia(request):
    return render(request, 'noticias/noticia1.html')