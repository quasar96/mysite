from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
    context = {
        'products': ['Товар 1', 'Товар 2', 'Товар 3'],
    }
    return render(request, 'main/index.html', context)

def python(request):
    return render(request, 'main/python.html')