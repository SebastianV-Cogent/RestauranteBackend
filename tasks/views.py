import json
from django.http import HttpResponse
from django.http.response import JsonResponse
from tasks.models import Usuario, Sucursales, Intolerancias, Ingredientes, Necesidades, Preferencias, Enfermedades, ListaIntolerancias, ListaNecesidades, ListaAlergias, ListaEnfermedades, ListaIngredientes, ListaPedidos, ListaPreferencias, Platillos, Pedidos
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
# Create your views here.

######################################################### CRUD DEL USUARIO #################################################
@csrf_exempt
def crearUsuario(request):
  if request.method=='POST':
    payload = json.loads(request.body.decode('utf-8'))

    necesidad_id = payload.get('necesidad_id')
    necesidad_instancia = Necesidades.objects.get(id=necesidad_id)

    # Similarmente, haz lo mismo para la preferencia si es necesario
    preferencia_id = payload.get('preferencia_id')
    preferencia_instancia = Preferencias.objects.get(id=preferencia_id)

    usuarioCreado = Usuario(
      nombre = payload.get('nombre'),
      edad = payload.get('edad'),
      genero = payload.get('genero'),
      telefono = payload.get('telefono'),
      password = payload.get('password'),
      necesidad = necesidad_instancia,
      preferencia = preferencia_instancia
    )
    usuarioCreado.save()
    return JsonResponse({"message": "Usuario creado exitosamente"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)

@csrf_exempt
def actualizarUsuario(request):
  if request.method=='PUT':
    payload = json.loads(request.body.decode('utf-8'))
    id = payload.get('id')
    usuario = Usuario.objects.get(id=id) ##obtener el usuario en base a su id

    usuario.nombre = payload.get('nombre', usuario.nombre)
    usuario.edad = payload.get('edad', usuario.edad)
    usuario.genero = payload.get('genero', usuario.genero)
    usuario.telefono = payload.get('telefono', usuario.telefono)
    usuario.password = payload.get('password', usuario.password)

    usuario.save()
    return JsonResponse(usuario, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)

@csrf_exempt
def obtenerUsuario(request):
  if request.method=='POST':
    payload = json.loads(request.body.decode('utf-8'))
    telefono = payload.get('telefono')
    password=payload.get('password')
    usuario=list(Usuario.objects.filter(telefono=telefono, password=password).values())
    return JsonResponse(usuario, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)

######################################################### CRUD DEL RESTAURANTE #############################################
@csrf_exempt
def crearSucursal(request):
  if request.method=='POST':
    payload = json.loads(request.body.decode('utf-8'))
    sucursalCreada = Sucursales(
      nombre = payload.get('nombre'),
      direccion = payload.get('direccion'),
      latitud = payload.get('latitud'),
      longitud = payload.get('longitud'),
    )
    sucursalCreada.save()
    return JsonResponse({"message": "Sucursal creada exitosamente"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)

@csrf_exempt
def actualizarSucursal(request):
  if request.method=='PUT':
    payload = json.loads(request.body.decode('utf-8'))
    id = payload.get('id')
    sucursal = Sucursales.objects.get(id=id)

    sucursal.nombre = payload.get('nombre', sucursal.nombre)
    sucursal.direccion = payload.get('direccion', sucursal.direccion)
    sucursal.latitud = payload.get('latitud', sucursal.latitud)
    sucursal.longitud = payload.get('longitud', sucursal.longitud)

    sucursal.save()
    sucursal_serializado = serializers.serialize('json', [sucursal])
    return JsonResponse({"message": "Sucursal actualizada exitosamente", "data": sucursal_serializado}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)

@csrf_exempt
def obtenerSucursal(request):
  if request.method=='POST':
    payload = json.loads(request.body.decode('utf-8'))
    id = payload.get('id')
    sucursal = list(Sucursales.objects.filter(id=id).values())
    return JsonResponse(sucursal, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def obtenerTodasLasSucursales(request):
  if request.method=='GET':
    sucursales = list(Sucursales.objects.all().values())
    return JsonResponse(sucursales, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def eliminarSucursal(request):
  if request.method=='DELETE':
    payload = json.loads(request.body.decode('utf-8'))
    id = payload.get('id')
    sucursalEliminada = Sucursales.objects.get(id=id)
    sucursalEliminada.delete()
    return JsonResponse({"message": "Sucursal eliminada"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)

####################################################### CRUD DE INTOLERANCIAS ##############################################
@csrf_exempt
def crearIntolerancias(request):
  if request.method=='POST':
    payload = json.loads(request.body.decode('utf-8'))
    intoleranciaCreada = Intolerancias(
      nombre = payload.get('nombre')
    )
    intoleranciaCreada.save()
    return JsonResponse({"message": "Intolerancia agregada"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def crearListaIntolerancias(request):
  if request.method=='POST':
    payload = json.loads(request.body.decode('utf-8'))

    for intolerancia in payload.get('intolerancias'):
      idUsuario = intolerancia.get('idUsuario')
      idUsuario_instancia = Usuario.objects.get(id=idUsuario)
      idIntolerancia = intolerancia.get('idIntolerancia')
      idIntolerancia_instancia = Intolerancias.objects.get(id=idIntolerancia)

      listaCreada = ListaIntolerancias(
        usuario = idUsuario,
        intolerancias = idIntolerancia
      )
      listaCreada.save()
    return JsonResponse({"message": "Lista de intolerancias agregada"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def obtenerIntolerancias(request):
  if request.method=='GET':
    intolerancias = Intolerancias.objects.all().values()
    return JsonResponse(intolerancias, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
####################################################### CRUD DE INGREDIENTES ###############################################
@csrf_exempt
def crearIngredientes(request):
  if request.method=='POST':
    payload = json.loads(request.body.decode('utf-8'))
    ingredienteCreado = Ingredientes(
      nombre = payload.get('nombre')
    )
    ingredienteCreado.save()
    return JsonResponse({"message": "Ingrediente agregado"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def actualizarIngredientes(request):
  if request.method=='PUT':
    payload = json.loads(request.body.decode('utf-8'))
    id = payload.get('id')
    ingrediente = Ingredientes.objects.get(id=id)

    ingrediente.nombre = payload.get('nombre', ingrediente.nombre)
    ingrediente.save()
    return JsonResponse({"message": "Ingrediente actualizado"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def crearListaIngredientes(request):
  if request.method=='POST':
    payload = json.loads(request.body.decode('utf-8'))

    for item in payload.get('ingredientes'):
      idPlatillo = item.get('idPlatillo')
      idPlatillo_instancia = Platillos.objects.get(id=idPlatillo)
      idIngrediente = item.get('idIngrediente')
      idIngrediente_instancia = Ingredientes.objects.get(id=idIngrediente)

      listaCreada = ListaIngredientes(
        platillo = idPlatillo,
        ingredientes = idIngrediente
      )
      listaCreada.save()
    return JsonResponse({"message": "Lista de ingredientes agregada"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def obtenerIngredientes(request):
  if request.method=='GET':
    ingredientes = list(Ingredientes.objects.all().values())
    return JsonResponse(ingredientes, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def eliminarIngrediente(request):
  if request.method=='DELETE':
    payload = json.loads(request.body.decode('utf-8'))
    id = payload.get('id')
    ingredienteEliminado = Ingredientes.objects.get(id=id)
    ingredienteEliminado.delete()
    return JsonResponse({"message": "Ingrediente eliminado"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
####################################################### CRUD DE NECESIDADES ################################################
@csrf_exempt
def crearNecesidades(request):
  if request.method=='POST':
    payload = json.loads(request.body.decode('utf-8'))
    necesidadCreada = Necesidades(
      nombre = payload.get('nombre')
    )
    necesidadCreada.save()
    return JsonResponse({"message": "Necesidad agregada"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def crearListaNecesidades(request):
  if request.method=='POST':
    payload = json.loads(request.body.decode('utf-8'))

    for item in payload.get('necesidades'):
      idUsuario = item.get('idUsuario')
      idUsuario_instancia = Usuario.objects.get(id=idUsuario)
      idNecesidad = item.get('idNecesidad')
      idNecesidad_instancia = Necesidades.objects.get(id=idNecesidad)

      listaCreada = ListaNecesidades(
        usuario = idUsuario,
        neecesidades = idNecesidad
      )
      listaCreada.save()
    return JsonResponse({"message": "Lista de necesidades agregada"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def obtenerNecesidades(request):
  if request.method=='GET':
    necesidades = list(Necesidades.objects.all().values())
    return JsonResponse(necesidades, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
####################################################### CRUD DE PREFERENCIAS ###############################################
@csrf_exempt
def crearPreferencias(request):
  if request.method=='POST':
    payload = json.loads(request.body.decode('utf-8'))
    preferenciaCreada = Preferencias(
      nombre = payload.get('nombre')
    )
    preferenciaCreada.save()
    return JsonResponse({"message": "Preferencia agregada"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def crearListaPreferencias(request):
  if request.method=='POST':
    payload = json.loads(request.body.decode('utf-8'))

    for item in payload.get('preferencias'):
      idUsuario = item.get('idUsuario')
      idUsuario_instancia = Usuario.objects.get(id=idUsuario)
      idPreferencia = item.get('idPreferencia')
      idPreferencia_instancia = Preferencias.objects.get(id=idPreferencia)

      listaCreada = ListaPreferencias(
        usuario = idUsuario,
        preferencias = idPreferencia
      )
      listaCreada.save()
    return JsonResponse({"message": "Lista de preferencias agregada"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def obtenerPreferencias(request):
  if request.method=='GET':
    preferencias = list(Preferencias.objects.all().values())
    return JsonResponse(preferencias, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
####################################################### CRUD DE ENFERMEDADES ###############################################
@csrf_exempt
def crearEnfermedad(request):
  if request.method=='POST':
    payload = json.loads(request.body.decode('utf-8'))
    enfermedadCreada = Enfermedades(
      nombre = payload.get('nombre')
    )
    enfermedadCreada.save()
    return JsonResponse({"message": "Enfermedad agregada"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def crearListaEnfermedades(request):
  if request.method=='POST':
    payload = json.loads(request.body.decode('utf-8'))

    for item in payload.get('enfermedades'):
      idUsuario = item.get('idUsuario')
      idUsuario_instancia = Usuario.objects.get(id=idUsuario)
      idEnfermedad = item.get('idEnfermedad')
      idEnfermedad_instancia = Enfermedades.objects.get(id=idEnfermedad)

      listaCreada = ListaEnfermedades(
        usuario = idUsuario,
        enfermedades = idEnfermedad
      )
      listaCreada.save()
    return JsonResponse({"message": "Lista de enfermedades agregada"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def crearListaAlergias(request):
  if request.method=='POST':
    payload = json.loads(request.body.decode('utf-8'))

    for item in payload.get('alergias'):
      idUsuario = item.get('idUsuario')
      idUsuario_instancia = Usuario.objects.get(id=idUsuario)
      idIngrediente = item.get('idIngrediente')
      idIngrediente_instancia = Ingredientes.objects.get(id=idIngrediente)

      listaCreada = ListaAlergias(
        usuario = idUsuario,
        ingredientes = idIngrediente
      )
      listaCreada.save()
    return JsonResponse({"message": "Lista de alergias agregada"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)

@csrf_exempt
def obtenerEnfermedades(request):
  if request.method=='GET':
    enfermedades = list(Enfermedades.objects.all().values)
    return JsonResponse(enfermedades, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)

####################################################### CRUD DE PEDIDOS ####################################################
@csrf_exempt
def crearPedido(request):
  if request.method=='POST':
    payload = json.loads(request.body.decode('utf-8'))
    idUsuario = payload.get('idUsuario')
    idUsuario_instancia = Usuario.objects.get(id=idUsuario)
    pedidoCreado = Pedidos(
      usuario = idUsuario_instancia
    )
    pedidoCreado.save()
    return JsonResponse({"message": "Pedido agregado"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def obtenerTodosLosPedidos(request):
  if request.method=='GET':
    pedidos = list(Pedidos.objects.all().values())
    return JsonResponse(pedidos, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def obtenerPedido(request):
  if request.method=='POST':
    payload = json.loads(request.body.decode('utf-8'))
    id = payload.get('id')
    pedido = list(Pedidos.objects.filter(id=id).values())
    return JsonResponse(pedido, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def crearListaPedidos(request):
  if request.method=='POST':
    payload = json.loads(request.body.decode('utf-8'))

    for item in payload.get('pedidos'):
      idUsuario = item.get('idUsuario')
      idUsuario_instancia = Usuario.objects.get(id=idUsuario)
      idPedido = item.get('idPedido')
      idPedido_instancia = Pedidos.objects.get(id=idPedido)
      idPlatillo = item.get('idPlatillo')
      idPlatillo_instancia = Platillos.objects.get(id=idPlatillo)

      listaCreada = ListaPedidos(
        usuario = idUsuario,
        pedido = idPedido,
        platillo = idPlatillo
      )
      listaCreada.save()
    return JsonResponse({"message": "Lista de pedidos agregada"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def eliminarPedido(request):
  if request.method=='DELETE':
    payload = json.loads(request.body.decode('utf-8'))
    id = payload.get('id')
    pedidoEliminado = Pedidos.objects.get(id=id)
    pedidoEliminado.delete()
    return JsonResponse({"message": "Pedido eliminado"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
####################################################### CRUD DE PLATILLOS ##################################################
@csrf_exempt
def obtenerPlatillosRecomendados(request):
  if request.method=='POST':
    payload = json.loads(request.body.decode('utf-8'))
    nombre_usuario = payload.get('nombre')
    with connection.cursor() as cursor:
        cursor.callproc('recomendar_platillos', [nombre_usuario])
        results = cursor.fetchall()
    result_serialziado = serializers.serialize('json', results)
    return JsonResponse({"data": result_serialziado}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def obtenerTodosLosPlatillos(request):
  if request.method=='GET':
    platillos = list(Platillos.objects.all().values())
    return JsonResponse(platillos, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def crearPlatillo(request):
  if request.method=='POST':
    payload = json.loads(request.body.decode('utf-8'))
    idPreferencia = payload.get('idPreferencia')
    idPreferencia_instancia = Preferencias.objects.get(id=idPreferencia)
    platilloCreado = Platillos(
      nombre = payload.get('nombre'),
      descripcion = payload.get('descripcion'),
      costo = payload.get('costo'),
      url_imagen = payload.get('url_imagen'),
      platillo_dia = payload.get('platillo_dia'),
      preferencias_id = idPreferencia
    )
    platilloCreado.save()
    return JsonResponse({"message": "Platillo agregado"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def actualizarPlatillo(request):
  if request.method=='PUT':
    payload = json.loads(request.body.decode('utf-8'))
    idPreferencia = payload.get('idPreferencia')
    idPreferencia_instancia = Preferencias.objects.get(id=idPreferencia)
    platilloCreado = Platillos(
      nombre = payload.get('nombre'),
      descripcion = payload.get('descripcion'),
      costo = payload.get('costo'),
      url_imagen = payload.get('url_imagen'),
      platillo_dia = payload.get('platillo_dia'),
      preferencias_id = idPreferencia
    )
    platilloCreado.save()
    return JsonResponse({"message": "Platillo agregado"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def eliminarPlatillo(request):
  if request.method=='DELETE':
    payload = json.loads(request.body.decode('utf-8'))
    id = payload.get('id')
    platilloEliminado = Platillos.objects.get(id=id)
    platilloEliminado.delete()
    return JsonResponse({"message": "Platillo eliminado"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)