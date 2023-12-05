from django.http import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.

from django.http import HttpResponse

def inicio_view(request):
    return render(request, "AppCoder/inicio.html")

def view_inicio(xx):
    #return HttpResponse("Bienvenidos ...!!!")
     return render(xx, "AppCoder/padre.html")

def view_arrendador(xx):
    #return HttpResponse("Aqui voy a mostrar el arrendador ...!!!")
     return render(xx,"AppCoder/padre.html")

def view_arrendatario(xx):
    pass

def view_inmuebles():
    pass

def view_tipo_inmueble():
    pass

def view_pais():
    pass 
