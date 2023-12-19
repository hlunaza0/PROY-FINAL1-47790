from django.contrib import admin

# Register your models here.


from . import models

admin.site.register(models.Pais)
admin.site.register(models.Tipo_inmueble)
admin.site.register(models.Arrendador)
admin.site.register(models.Arrendatario)
admin.site.register(models.Inmueble)

admin.site.register(models.Avatar)

