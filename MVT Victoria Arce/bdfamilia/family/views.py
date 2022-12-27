from django.shortcuts import render
from django.http import HttpResponse

from family.models import Relative

def create_relative(request):
    Relative.objects.create(name = 'Maria', lastname = 'Arce', conection = 'Hermana', age = 29, lives_in_bahia = True)
    return HttpResponse('Nuevo familiar creado')

def list_relatives(request):
    all_relatives = Relative.objects.all()
    context = {
         'relatives' : all_relatives,
    }
    return render(request, 'list_relatives.html', context = context)