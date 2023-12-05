
from django.urls import path
from AppCoder.views import inicio_view, view_arrendador

app_name = "AppCoder"


urlpatterns = [
    path("inicio/", inicio_view, name="inicio"),
    path("arrendador/", view_arrendador),
]


