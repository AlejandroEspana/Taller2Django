from django import forms
from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = '__all__'
        widgets = {
            'fecha_solicitud': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nombre_solicitante': forms.TextInput(attrs={'class': 'form-control'}),
            'documento_identidad': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono_contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_solicitud': forms.Select(attrs={'class': 'form-select'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion_detallada': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'archivo_adjunto': forms.FileInput(attrs={'class': 'form-control'}),
        }
