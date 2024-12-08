from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def fun(request):
    return render(request, 'function_page.html')

class class_fun(TemplateView):
    template_name = 'class_page.html'
