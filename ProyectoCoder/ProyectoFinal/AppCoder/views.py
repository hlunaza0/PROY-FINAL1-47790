from django.http import HttpResponse
from django.shortcuts import redirect, render

from . import models
from .models import Pais, Tipo_inmueble, Arrendador, Arrendatario, Inmueble

from .forms import PaisFormulario, TipoInmuebleFormulario, ArrendadorFormulario, ArrendatarioFormulario, InmuebleFormulario, InmuebleBuscarFormulario



# Create your views here.

from django.http import HttpResponse

def inicio_view(request):
    return render(request, "AppCoder/inicio.html")

def view_inicio(xx):
    #return HttpResponse("Bienvenidos ...!!!")
     return render(xx, "AppCoder/padre.html")


def crea_pais(request):

    if request.method == "POST":
      
        miFormulario = PaisFormulario(request.POST)
    
        if miFormulario.is_valid():
           data = miFormulario.cleaned_data
           pais = Pais(nombre=data["nombre"])
           pais.save()
           return redirect('AppCoder:inicio')
        
        return render(request, "AppCoder/paisFormulario.html",{"miFormulario":miFormulario})
    
    else:
      
        miFormulario = PaisFormulario()

        return render(request, "AppCoder/PaisFormulario.html",{"miFormulario":miFormulario})
    

def crea_tipoInmueble(request):

    if request.method == "POST":
      
        miFormulario = TipoInmuebleFormulario(request.POST)
    
        if miFormulario.is_valid():
           data = miFormulario.cleaned_data
           tipoinmueble = Tipo_inmueble(nombre=data["nombre"])
           tipoinmueble.save()
           return redirect('AppCoder:inicio')
        
        return render(request, "AppCoder/tipoinmuebleFormulario.html",{"miFormulario":miFormulario})
    
    else:

        miFormulario = TipoInmuebleFormulario()

        return render(request, "AppCoder/tipoinmuebleFormulario.html",{"miFormulario":miFormulario})


def crea_arrendador(request):

    if request.method == "POST":
      
        miFormulario = ArrendadorFormulario(request.POST)
    
        if miFormulario.is_valid():
           data = miFormulario.cleaned_data
           arrendador = Arrendador(dni=data["dni"], nombre=data["nombre"], apellido=data["apellido"], email=data["email"],domicilio=data["domicilio"] )
           arrendador.save()
           return redirect('AppCoder:inicio')
        
        return render(request, "AppCoder/arrendadorFormulario.html",{"miFormulario":miFormulario})
    
    else:
       
        miFormulario = ArrendadorFormulario()

        return render(request, "AppCoder/arrendadorFormulario.html",{"miFormulario":miFormulario})



def crea_arrendatario(request):

    if request.method == "POST":
      
        miFormulario = ArrendatarioFormulario(request.POST)
    
        if miFormulario.is_valid():
           data = miFormulario.cleaned_data
           arrendatario = Arrendatario(dni=data["dni"], nombre=data["nombre"], apellido=data["apellido"], email=data["email"],domicilio=data["domicilio"] )
           arrendatario.save()
           return redirect('AppCoder:inicio')
        
        return render(request, "AppCoder/arrendatarioFormulario.html",{"miFormulario":miFormulario})
    
    else:
        
        miFormulario = ArrendadorFormulario()

        return render(request, "AppCoder/arrendatarioFormulario.html",{"miFormulario":miFormulario})


def crea_inmueble(request):

    if request.method == "POST":
      
        miFormulario = InmuebleFormulario(request.POST)
    
        if miFormulario.is_valid():
           data = miFormulario.cleaned_data
           inmueble = Inmueble(nombre=data["nombre"], medidas=data["medidas"], precio=data["precio"],direccion=data["direccion"], tipo=data["tipo"])
           inmueble.save()
           return redirect('AppCoder:inicio')
        
        return render(request, "AppCoder/inmuebleFormulario.html",{"miFormulario":miFormulario})
    
    else:
        
        miFormulario = InmuebleFormulario()

        return render(request, "AppCoder/inmuebleFormulario.html",{"miFormulario":miFormulario})


def Lista_inmueble(request):
    
    inmueble = Inmueble.objects.all()

    return render(request,"AppCoder/leerInmueble.html", {inmueble:inmueble})




def inmueble_buscar_view(request):
    if request.method == "GET":
        form = InmuebleBuscarFormulario()
        return render(
            request,
            "AppCoder/inmuebleBuscaFormulario.html",
            context={"form": form}
        )
    else:
        formulario = InmuebleBuscarFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            inmueble_filtrados = []
            for inmueble in Inmueble.objects.filter(nombre=informacion["nombre"]):
                inmueble_filtrados.append(inmueble)

            contexto = {"inmueble": inmueble_filtrados}
            return render(request, "AppCoder/inmuebleBuscaFormulario.html", contexto)


    