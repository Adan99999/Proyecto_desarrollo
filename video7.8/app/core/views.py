from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
# return HttpResponse('hola esta es nu primera url')
def myfirstview(request):

    data = {
        'name': 'Adan'
    }
    return render(request, 'index.html', data)