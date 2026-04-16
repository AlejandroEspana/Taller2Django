from django.urls import path
from . import views

app_name = 'solicitudes'

urlpatterns = [
    path('crear/', views.crear_solicitud, name='crear'),
    path('confirmacion/', views.confirmacion_solicitud, name='confirmacion'),
]
