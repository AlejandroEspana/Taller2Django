from django.contrib import admin
from .models import Asistencia

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'documento_identidad', 'fecha_asistencia', 'presente', 'fecha_registro')
    list_filter = ('presente', 'fecha_asistencia')
    search_fields = ('nombre_completo', 'documento_identidad', 'correo_electronico')
    readonly_fields = ('fecha_registro',)
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre_completo', 'documento_identidad', 'correo_electronico')
        }),
        ('Datos de Asistencia', {
            'fields': ('fecha_asistencia', 'hora_ingreso', 'hora_salida', 'presente')
        }),
        ('Información Adicional', {
            'fields': ('observaciones', 'fecha_registro')
        }),
    )
