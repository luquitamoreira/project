from django.http import HttpResponse


def saludo(request):
    return HttpResponse("HOLA DJANGO : Lucas.")

def segunda_vista(request):
    return HttpResponse("<h1>Hola segunda funcion de views.py</h1>")

def nombre(request,nombre:str,apellido:str):
    nombre= nombre.capitalize()
    apellido=apellido.capitalize()
    return HttpResponse(f'{apellido},{nombre}')

def probando_template(request):