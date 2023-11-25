import uuid
from django.db import models

# Create your models here.

class Platillo(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  nombre = models.TextField(max_length=255)
  lista_ingredientes = models.ForeignKey("ListaIngredientes", on_delete=models.CASCADE)
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
  
class Usuario(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  nombre = models.TextField(max_length=100)
  edad = models.IntegerField()
  genero = models.TextField(max_length=10)
  telefono = models.TextField(max_length=10)
  lista_preferencias = models.ForeignKey("ListaPreferencias", on_delete=models.CASCADE)
  lista_enfermedades = models.ForeignKey("ListaEnfermedades", on_delete=models.CASCADE)
  lista_necesidades = models.ForeignKey("ListaNecesidades", on_delete=models.CASCADE)
  lista_intolerancias = models.ForeignKey("ListaIntolerancias", on_delete=models.CASCADE)
  created_at = models.DateField(auto_now_add=True)

class ListaEnfermedades(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  id_usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
  enfermedades = models.ForeignKey("Enfermedad", on_delete=models.CASCADE)
  created_at = models.DateField(auto_now_add=True)

class ListaIntolerancias(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  id_usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
  intolerancias = models.ForeignKey("Intolerancias", on_delete=models.CASCADE)
  created_at = models.DateField(auto_now_add=True)

class ListaNecesidades(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  id_usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
  necesidades = models.ForeignKey("Necesidades", on_delete=models.CASCADE)
  created_at = models.DateField(auto_now_add=True)

class ListaPreferencias(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  id_usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
  preferencias = models.ForeignKey("Preferencias", on_delete=models.CASCADE)
  created_at = models.DateField(auto_now_add=True)



