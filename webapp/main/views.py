from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    data = {
        'title': 'Головна сторінка',
        'values': [],
        'obj': {
            }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return HttpResponse('Контакти')
