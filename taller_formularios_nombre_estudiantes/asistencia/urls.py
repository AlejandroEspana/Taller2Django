from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario_asistencia, name='formulario_asistencia'),
    path('confirmacion/<int:id>/', views.confirmacion_asistencia, name='confirmacion_asistencia'),
]
