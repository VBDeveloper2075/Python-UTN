from django.shortcuts import render
from django.http import HttpResponse

"""def index(request):
    return HttpResponse("Hola Mundo!.")"""


def index(request):
    contenido = { 'nombre_sitio': 'LibrosOnline' }
    return render(request, 'compras/index.html', contenido)

