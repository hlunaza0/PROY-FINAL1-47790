
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

from AppCoder.views import (
     inicio_view, 
     crea_pais,
     crea_tipoInmueble,
     crea_arrendador,
     crea_arrendatario,
     crea_inmueble,
     Lista_inmueble,
     inmueble_buscar,
     ### CRUD
     lista_pais,
     elimina_pais,
     editar_pais,
     PaisListView,
     PaisDetail,
     PaisCreateView,
     PaisUpdateView,
     PaisDeleteView,
     PaisCreateView,
     ### LOGIN
     login_view,
     registro_view,
     ###### EDITAR USUARIO
     editar_perfil_view,
     crear_avatar_view,
     ###### ACERCA AUTOR
     acerca_autor_view,
     listar_usuarios_view,
     listar_inmuebles_view,

     )

app_name = "AppCoder"


urlpatterns = [
    path("inicio/", inicio_view, name="inicio"),
    path("Lista-inmueble/",Lista_inmueble, name="Lista-inmueble"),
    path("inmueble-buscar", inmueble_buscar, name="inmueble-buscar"),
    path("lista-pais", lista_pais, name="lista-pais"),
    ###### CRUD
    path("crea-pais/",crea_pais, name="crea-pais"),
    path("editar-pais/<int:id>",editar_pais, name="editar-pais"),
    path("elimina-pais/<int:id>",elimina_pais, name="elimina-pais"),
    path("crea-tipoinmueble/",crea_tipoInmueble, name="crea-tipoinmueble"),
    path("crea-arrendador/",crea_arrendador, name="crea-arrendador"),
    path("crea-arrendatario/",crea_arrendatario, name="crea-arrendatario"),
    path("crea-inmueble/",crea_inmueble, name="crea-inmueble"),
    ###### CBV
    path("pais_list/",PaisListView.as_view(), name="pais_list"),
    path("pais/new",PaisCreateView.as_view(), name="pais-create"),
    path("pais/<pk>",PaisDetail.as_view(), name="pais-details"),
    path("pais/<pk>/update",PaisUpdateView.as_view(), name="pais-update"),
    path("pais/<pk>/delete",PaisDeleteView.as_view(), name="pais-delete"),
    ###### LOGIN
    path("registro", registro_view, name="registro"),
    path("login", login_view, name="login"),
    path("logout", LogoutView.as_view(template_name="AppCoder/logout.html"), name="logout"),
    ###### EDITAR USUARIO
    path("editar-perfil", editar_perfil_view, name="editar-perfil"),
    path("crear-avatar", crear_avatar_view, name="crear-avatar"),
    ###### ACERCA DE MI
    path("route about/", acerca_autor_view, name="acer-auto"),
    ###### LISTADO DE USUARIO
    path("accounts/signup", listar_usuarios_view, name='listar_usuarios'),
    ###### LISTADO DE INMUEBLES
    path("route pages/",listar_inmuebles_view, name="listar_inmuebles"),

    

]


