from django import forms
from . models import Inmueble

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
      medidas = forms.CharField()
