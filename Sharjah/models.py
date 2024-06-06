from django.db import models

# Create your models here.

class Propiedad(models.Model):
    TIPO_CHOICES = [
        ('casa', 'Casa'),
        ('apartamento', 'Apartamento'),
        ('villa', 'Villa'),
        ('terreno', 'Terreno'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    habitaciones = models.PositiveIntegerField()
    banos = models.PositiveIntegerField()
    metros_cuadrados = models.PositiveIntegerField()
    ubicacion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='propiedades', null=True, blank=True)

    def _str_(self):
        return self.titulo

class Agente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    foto = models.ImageField(upload_to='agentes', null=True, blank=True)

    def _str_(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def _str_(self):
        return self.nombre