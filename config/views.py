from django.http import HttpResponse

def saludo(request):
    return HttpResponse("HOLA DJANGO : Lucas.")

def segunda_vista(request):
    return HttpResponse("<h1>Hola segunda funcion de views.py</h1>")