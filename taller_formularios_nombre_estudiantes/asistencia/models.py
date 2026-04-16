from django.db import models

class Asistencia(models.Model):
    nombre_completo = models.CharField(max_length=150)
    documento_identidad = models.CharField(max_length=50)
    correo_electronico = models.EmailField()
    fecha_asistencia = models.DateField()
    hora_ingreso = models.TimeField()
    hora_salida = models.TimeField(blank=True, null=True)
    presente = models.BooleanField(default=True)
    observaciones = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"{self.nombre_completo} - {self.fecha_asistencia}"
