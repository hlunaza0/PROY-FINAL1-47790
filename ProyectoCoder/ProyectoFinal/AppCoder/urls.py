
from django.urls import path
from AppCoder.views import (
     inicio_view, 
     crea_pais,
     crea_tipoInmueble,
     crea_arrendador,
     crea_arrendatario,
     crea_inmueble,
     Lista_inmueble,
     inmueble_buscar_view)

app_name = "AppCoder"


urlpatterns = [
    path("inicio/", inicio_view, name="inicio"),
    path("crea-pais/",crea_pais, name="crea-pais"),
    path("crea-tipoinmueble/",crea_tipoInmueble, name="crea-tipoinmueble"),
    path("crea-arrendador/",crea_arrendador, name="crea-arrendador"),
    path("crea-arrendatario/",crea_arrendatario, name="crea-arrendatario"),
    path("crea-inmueble/",crea_inmueble, name="crea-inmueble"),
    path("Lista-inmueble/",Lista_inmueble, name="Lista-inmueble"),
    path("inmueble-buscar", inmueble_buscar_view, name="inmueble-buscar"),
   
]


