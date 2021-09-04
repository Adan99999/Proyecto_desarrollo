from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
# return HttpResponse('hola esta es nu primera url')
from core.models import Category, Product


def myfirstview(request):

    data = {
        'name': 'Adan',
        'categories': Category.objects.all()
    }
    return render(request, 'home.html', data)


def mysecondview(request):

    data = {
        'name': 'Adan',
        'categories': Category.objects.all(),
        'products': Product.objects.all()
    }
    return render(request, 'second.html', data)
