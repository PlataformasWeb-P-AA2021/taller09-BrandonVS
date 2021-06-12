from django.contrib import admin

from ordenamiento.models import Parroquia, Barrio
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class ParroquiaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = ('nombre', 'tipo_parroquia')
    search_fields = ('nombre',)

admin.site.register(Parroquia, ParroquiaAdmin)

class BarrioAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios', 'parroquia')
    search_fields = ('parroquia__nombre', 'barrio__nombre')

admin.site.register(Barrio, BarrioAdmin)
