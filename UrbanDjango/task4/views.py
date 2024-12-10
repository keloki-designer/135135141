from django.shortcuts import render

# Create your views here.

def home(request):
    title = 'Moto 365'
    context = {
        'title': title,
    }
    return render(request, 'fourth_task/platform.html', context)


def moto(request):
    moto_catalog = ['Дорожные', 'Спортивные', 'Чоперы', 'Эндуро']
    title = 'Moto 365'
    context = {
        'moto_catalog': moto_catalog,
        'title': title,
    }
    return render(request, 'fourth_task/moto.html', context)


def basket(request):
    title = 'Moto 365'
    context = {
        'title': title,
    }
    return render(request,'fourth_task/basket.html', context)



