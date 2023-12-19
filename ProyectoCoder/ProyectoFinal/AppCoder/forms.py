from django import forms
from . models import Inmueble
from . models import Pais

class PaisFormulario(forms.Form):
      nombre = forms.CharField()
  

class TipoInmuebleFormulario(forms.Form):
      nombre = forms.CharField()


class ArrendadorFormulario(forms.Form):
      dni = forms.CharField(max_length=12) 
      nombre = forms.CharField(max_length=30)
      apellido = forms.CharField(max_length=30)
      email = forms.EmailField()
      domicilio = forms.CharField(max_length=50)


class ArrendatarioFormulario(forms.Form):
      dni = forms.CharField(max_length=12) 
      nombre = forms.CharField(max_length=30)
      apellido = forms.CharField(max_length=30)
      email = forms.EmailField()
      domicilio = forms.CharField(max_length=50)

class InmuebleFormulario(forms.ModelForm):
      # nombre = forms.CharField(max_length=12)
      # medidas = forms.CharField(max_length=20)
      # precio = forms.CharField(max_length=10)
      # direccion = forms.CharField(max_length=50)
      # tipo_id = forms.IntegerField()     

      class Meta:
            model=Inmueble
            fields="__all__"

      # def __init__(self, *args, **kwargs):
      #       super(InmuebleFormulario, self).__init__(*args, **kwargs)
      #       self.fields['tipo'].queryset = Inmueble.objects.all()


class InmuebleBuscarFormulario(forms.Form):
      nombre = forms.CharField()
     #medidas = forms.CharField()


#### CLASE 23: registro

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserModel
from .models import Avatar


class UserCreationFormulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ["password1", "password2", "username", "email"]
        help_texts = {k: "" for k in fields}


class UserEditionFormulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = UserModel
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k: "" for k in fields}


class UserAvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ["imagen"]
