from django.http import HttpResponse
from django.shortcuts import redirect, render

from . import models
from .models import Pais, Tipo_inmueble, Arrendador, Arrendatario, Inmueble, Avatar

from .forms import PaisFormulario, TipoInmuebleFormulario, ArrendadorFormulario, ArrendatarioFormulario, InmuebleFormulario, InmuebleBuscarFormulario

# Create your views here.

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required


def inicio_view(request):
#   return render(request, "AppCoder/inicio.html")
    if request.user.is_authenticated:
        usuario = request.user
        avatar = Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""

    return render(request, "AppCoder/inicio.html", context={"avatar_url": avatar_url})

# def view_inicio(xx):
#     #return HttpResponse("Bienvenidos ...!!!")
#      return render(xx, "AppCoder/padre.html")


#******************************************************************
#****************    CREACION DE REGISTROS   **********************
#******************************************************************
@login_required
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

@login_required
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


@login_required
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

@login_required
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

#******************************************************************
#*****************    LISTADO DE ENTIDADES   **********************
#******************************************************************

def Lista_inmueble(request):
    
    inmueble = Inmueble.objects.all()

    return render(request,"AppCoder/inmueblelistado.html", {"inmueble":inmueble})


# def Lista_inmueble(request):
#     todos_los_inmuebles = []
#     for inmueble in Inmueble.objects.all():
#         todos_los_inmuebles.append(inmueble)

#     contexto = {"inmueble": todos_los_inmuebles}
#     return render(request, "AppCoder/inmueblelistado.html", contexto)

#******************************************************************
#*****************    BUSQEDA DE INMUEBLE    **********************
#******************************************************************

def inmueble_buscar(request):
    if request.method == "GET":
        form = InmuebleBuscarFormulario()
        return render(
            request,
            "AppCoder/inmuebleBuscaFormulario.html",
            context={"form":form}
        )
    else:
        formulario = InmuebleBuscarFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            inmueble_filtrados = []
            for inmueblex in Inmueble.objects.filter(nombre=informacion["nombre"]):
                inmueble_filtrados.append(inmueblex)

            contexto = {"inmueble": inmueble_filtrados}
            return render(request, "AppCoder/inmueblelistado.html", contexto)


#******************************************************************
#********************      CRUD FUNCIONAL      ********************
#******************************************************************
        
######################## CREA PAIS  ########################
@login_required        
def lista_pais(request):

    pais = Pais.objects.all()

    return render(request,"AppCoder/paislistado.html", {"pais":pais})

######################## LISTA PAIS  ########################
@login_required
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

######################## ACTULAIZA PAIS  ########################
@login_required
def editar_pais(req, id):

    if req.method == "POST":
      
        miFormulario = PaisFormulario(req.POST)
    
        if miFormulario.is_valid():
           data = miFormulario.cleaned_data
           pais = Pais.objects.get(id=id)
          
           pais.nombre = data["nombre"]
           pais.save()
           return redirect('AppCoder:inicio')
        
        return render(req, "AppCoder/editarpais.html",{"miFormulario":miFormulario})
    
    else:
           pais = Pais.objects.get(id=id)
           
           miFormulario = PaisFormulario(initial={"nombre":pais.nombre})

           return render(req, "AppCoder/editarpais.html",{"miFormulario":miFormulario, "id":pais.id})
  
######################## ELIMINA PAIS  ########################
@login_required
def elimina_pais(req, id):

    if req.method == "POST":
        pais = Pais.objects.get(id=id) 
        pais.delete()

        pais = Pais.objects.all()

        return render(req,"AppCoder/paislistado.html", {"pais":pais})


#*************************************************************************
#*****************   "CRUD" Con vistas basadas en Clases  ****************
#*************************************************************************
#*******
#*** Pais CRUD create read update y delete
#*******

from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class PaisListView(LoginRequiredMixin, ListView):
    model = Pais
    template_name = 'AppCoder/cbv_pais_list.html'
    context_object_name = "pais"   

class PaisDetail(LoginRequiredMixin,DeleteView):
    model = Pais
    template_name = 'AppCoder/Pais_detail.html'
    context_object_name = "pais"   

class PaisCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Pais
    template_name = 'AppCoder/cbv_pais_create.html'
    success_url = reverse_lazy("AppCoder:pais_list") 
    fields = ["nombre"]

class PaisUpdateView(LoginRequiredMixin,UpdateView):
    model = Pais
    template_name = 'AppCoder/cbv_pais_update.html'
    success_url = reverse_lazy("AppCoder:pais_list") 
    fields = ["nombre"]
     

class PaisDeleteView(LoginRequiredMixin,DeleteView):
    model = Pais
    template_name = 'AppCoder/cbv_pais_delete.html'
    success_url = reverse_lazy("AppCoder:pais_list")


#################### CLASE 23:  Login / Logout #########################################
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

def login_view(request):

    if request.user.is_authenticated:
        return render(
            request,
            "AppCoder/inicio.html",
            {"mensaje": f"Ya estás autenticado: {request.user.username}"}
        )

    if request.method == "GET":
        return render(
            request,
            "AppCoder/login.html",
            {"form": AuthenticationForm()}
        )
    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            password = informacion["password"]

            modelo = authenticate(username=usuario, password=password)
            login(request, modelo)

            return render(
                request,
                "AppCoder/inicio.html",
                {"mensaje": f"Bienvenido {modelo.username}"}
            )
        else:
            return render(
                request,
                "AppCoder/login.html",
                {"form": formulario}
            )



def logout_view(request):
    pass


from .forms import UserCreationFormulario, UserEditionFormulario
from django.contrib.auth.views import PasswordChangeView


def registro_view(request):

    if request.method == "GET":
        return render(
            request,
            "AppCoder/registro.html",
            {"form": UserCreationFormulario()}
        )
    else:
        formulario = UserCreationFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            formulario.save()

            return render(
                request,
                "AppCoder/inicio.html",
                {"mensaje": f"Usuario creado: {usuario}"}
            )
        else:
            return render(
                request,
                "AppCoder/registro.html",
                {"form": formulario}
            )
        
#################### CLASE 24:  Editar perfil #########################################

@login_required
def editar_perfil_view(request):

    usuario = request.user
    avatar = Avatar.objects.filter(user=usuario).last()
    avatar_url = avatar.imagen.url if avatar is not None else ""

 
    if request.method == "GET":


        valores_iniciales = {
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name
        }


        formulario = UserEditionFormulario(initial=valores_iniciales)
        return render(
            request,
            "AppCoder/editar_perfil.html",
            context={"form": formulario, "usuario": usuario, "avatar_url": avatar_url}
            )
    else:
        formulario = UserEditionFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data

            usuario.email = informacion["email"]

            usuario.set_password(informacion["password1"])

            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.save()
        return redirect("AppCoder:inicio")

from .forms import UserAvatarFormulario 

@login_required
def crear_avatar_view(request):

    usuario = request.user

    if request.method == "GET":
        formulario = UserAvatarFormulario()
        return render(
            request,
            "AppCoder/crear_avatar.html",
            context={"form": formulario, "usuario": usuario}
        )
    else:
        formulario = UserAvatarFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Avatar(user=usuario, imagen=informacion["imagen"])
            modelo.save()
            return redirect("AppCoder:inicio")

##### ACERCA DE MI
def acerca_autor_view(request):
     return render(request, "AppCoder/acercademi.html")        

##### LISTADO DE USUARIOS
from django.contrib.auth.models import User 

def listar_usuarios_view(request):
    usuarios = User.objects.all()
    return render(request, 'AppCoder/usuario_list.html', {'usuarios': usuarios})

##### LISTADO DE INMUEBLES
def listar_inmuebles_view(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'AppCoder/inmueble_list.html', {'inmuebles': inmuebles})


