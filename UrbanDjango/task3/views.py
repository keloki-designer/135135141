from django.shortcuts import render

# Create your views here.

def home(request):
    title = 'Django'
    context = {
        'title': title,
    }
    return render(request, 'platform.html', context)

def moto(request):
    return render(request, 'moto.html')

def auto(request):
    return render(request, 'auto.html')

