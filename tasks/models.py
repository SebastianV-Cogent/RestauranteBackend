import uuid
from django.db import models

# Create your models here.

class Enfermedad(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    nombre = models.TextField(max_length=255)
    created_at = models.DateField(auto_now_add=True)

class Intolerancias(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    nombre = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    
class Necesidades(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    nombre = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)

class Preferencias(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    nombre = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)

class ListaEnfermedades(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    id_usuario = models.UUIDField()
    enfermedades = models.ManyToManyField(Enfermedad, related_name='listas_enfermedades')
    created_at = models.DateField(auto_now_add=True)

class ListaIntolerancias(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    id_usuario = models.UUIDField()
    intolerancias = models.ManyToManyField(Intolerancias, related_name='lista_intolerancias')
    created_at = models.DateField(auto_now_add=True)

class ListaNecesidades(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    id_usuario = models.UUIDField()
    necesidades = models.ManyToManyField(Necesidades, related_name='lista_necesidades')
    created_at = models.DateField(auto_now_add=True)

class ListaPreferencias(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    id_usuario = models.UUIDField()
    preferencias = models.ManyToManyField(Preferencias, related_name='lista_preferencias')
    created_at = models.DateField(auto_now_add=True)

class Usuario(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  nombre = models.TextField(max_length=100)
  edad = models.IntegerField()
  genero = models.TextField(max_length=10)
  telefono = models.TextField(max_length=10)
  lista_preferencias = models.ManyToManyField(ListaPreferencias, related_name='usuarios')
  lista_enfermedades = models.ManyToManyField(ListaEnfermedades, related_name='usuarios')
  lista_necesidades = models.ManyToManyField(ListaNecesidades, related_name='usuarios')
  lista_intolerancias = models.ManyToManyField(ListaIntolerancias, related_name='usuarios')
  created_at = models.DateField(auto_now_add=True)

