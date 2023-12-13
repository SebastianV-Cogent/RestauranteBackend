import uuid
from django.db import models

# Create your models here.

class Sucursales(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  nombre = models.TextField(max_length=255)
  direccion = models.TextField(max_length=255)
  latitud = models.DecimalField(decimal_places=5, max_digits=10)
  longitud = models.DecimalField(decimal_places=5, max_digits=10)

class Platillos(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  nombre = models.TextField(max_length=255)
  descripcion = models.TextField(max_length=255)
  costo = models.DecimalField(decimal_places=2,max_digits=10)
  preferencias = models.ForeignKey("Preferencias", on_delete=models.CASCADE)
  url_imagen = models.TextField(max_length=255)
  platillo_dia = models.BooleanField(default=False)

class IngredientesProhibidos(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  ingrediente = models.ForeignKey("Ingredientes", on_delete=models.CASCADE)
  enfermedad = models.ForeignKey("Enfermedades", on_delete=models.CASCADE)

class IngredientesRestringidos(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  necesidad = models.ForeignKey("Necesidades", on_delete=models.CASCADE)
  ingrediente = models.ForeignKey("Ingredientes", on_delete=models.CASCADE)

class Ingredientes(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  nombre = models.TextField(max_length=255)

class Enfermedades(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  nombre = models.TextField(max_length=255)

class Intolerancias(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  nombre = models.CharField(max_length=255)
    
class Necesidades(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  nombre = models.CharField(max_length=255)

class Preferencias(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  nombre = models.CharField(max_length=255)
  
class Usuario(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  nombre = models.TextField(max_length=100)
  edad = models.IntegerField()
  costoMaximo = models.DecimalField(decimal_places=2,max_digits=10)
  genero = models.TextField(max_length=10)
  telefono = models.TextField(max_length=10)
  password = models.TextField(max_length=255)
  necesidad = models.ForeignKey("Necesidades", on_delete=models.CASCADE)
  preferencia = models.ForeignKey("Preferencias", on_delete=models.CASCADE)

class Pedidos(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
  fecha = models.DateField(auto_now_add=True)

class IngredientesIntolerancias(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  intolerancias = models.ForeignKey("Intolerancias", on_delete=models.CASCADE)
  ingredientes = models.ForeignKey("Ingredientes", on_delete=models.CASCADE)


#####################################################AQUI VAN LAS LISTAS###########################################################
class ListaEnfermedades(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
  enfermedades = models.ForeignKey("Enfermedades", on_delete=models.CASCADE)

class ListaIntolerancias(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
  intolerancias = models.ForeignKey("Intolerancias", on_delete=models.CASCADE)

class ListaNecesidades(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
  necesidades = models.ForeignKey("Necesidades", on_delete=models.CASCADE)

class ListaPreferencias(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
  preferencias = models.ForeignKey("Preferencias", on_delete=models.CASCADE)

class ListaAlergias(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
  ingredientes = models.ForeignKey("Ingredientes", on_delete=models.CASCADE)

class ListaIngredientes(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  platillo = models.ForeignKey("Platillos", on_delete=models.CASCADE)
  ingredientes = models.ForeignKey("Ingredientes", on_delete=models.CASCADE)

class ListaPedidos(models.Model):
  id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
  platillo = models.ForeignKey("Platillos", on_delete=models.CASCADE)
  pedido = models.ForeignKey("Pedidos", on_delete=models.CASCADE)

