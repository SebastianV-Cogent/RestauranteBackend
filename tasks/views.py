import json
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
    usuario_serializado = serializers.serialize('json', [usuario])
    return JsonResponse({"message": "usuario actualizado exitosamente", "data": usuario_serializado}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)

@csrf_exempt
def obtenerUsuario(request):
  if request.method=='GET':
    payload = json.loads(request.body.decode('utf-8'))
    telefono = payload.get('telefono')
    password=payload.get('password')
    usuario = Usuario.objects.get(telefono=telefono, password=password)
    usuario_serializado = serializers.serialize('json', [usuario])
    return JsonResponse({"data": usuario_serializado}, safe=False)
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
    sucursal = Sucursales.objects.get(id=id) ##obtener el usuario en base a su id

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
  if request.method=='GET':
    payload = json.loads(request.body.decode('utf-8'))
    id = payload.get('id')
    sucursal = Sucursales.objects.get(id=id)
    sucursal_serializado = serializers.serialize('json', [sucursal])
    return JsonResponse({"data": sucursal_serializado}, safe=False)
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
        usuario = idUsuario_instancia,
        intolerancias = idIntolerancia_instancia
      )
      listaCreada.save()
    return JsonResponse({"message": "Lista de intolerancias agregada"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def obtenerIntolerancias(request):
  if request.method=='GET':
    intolerancias = Intolerancias.objects.all()
    intolerancias_serializado = serializers.serialize('json', intolerancias)
    return JsonResponse({"data": intolerancias_serializado}, safe=False)
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
def crearListaIngredientes(request):
  if request.method=='POST':
    payload = json.loads(request.body.decode('utf-8'))

    for item in payload.get('ingredientes'):
      idPlatillo = item.get('idPlatillo')
      idPlatillo_instancia = Platillos.objects.get(id=idPlatillo)
      idIngrediente = item.get('idIngrediente')
      idIngrediente_instancia = Ingredientes.objects.get(id=idIngrediente)

      listaCreada = ListaIngredientes(
        platillo = idPlatillo_instancia,
        ingredientes = idIngrediente
      )
      listaCreada.save()
    return JsonResponse({"message": "Lista de ingredientes agregada"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def obtenerIngredientes(request):
  if request.method=='GET':
    ingredientes = Ingredientes.objects.all()
    ingredientes_serializado = serializers.serialize('json', ingredientes)
    return JsonResponse({"data": ingredientes_serializado}, safe=False)
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
        usuario = idUsuario_instancia,
        neecesidades = idNecesidad_instancia
      )
      listaCreada.save()
    return JsonResponse({"message": "Lista de necesidades agregada"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def obtenerNecesidades(request):
  if request.method=='GET':
    necesidades = Necesidades.objects.all()
    necesidades_serializado = serializers.serialize('json', necesidades)
    return JsonResponse({"data": necesidades_serializado}, safe=False)
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
        usuario = idUsuario_instancia,
        preferencias = idPreferencia_instancia
      )
      listaCreada.save()
    return JsonResponse({"message": "Lista de preferencias agregada"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
@csrf_exempt
def obtenerPreferencias(request):
  if request.method=='GET':
    preferencias = Preferencias.objects.all()
    preferencias_serializado = serializers.serialize('json', preferencias)
    return JsonResponse({"data": preferencias_serializado}, safe=False)
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
        usuario = idUsuario_instancia,
        enfermedades = idEnfermedad_instancia
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
        usuario = idUsuario_instancia,
        ingredientes = idIngrediente_instancia
      )
      listaCreada.save()
    return JsonResponse({"message": "Lista de alergias agregada"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)

@csrf_exempt
def obtenerEnfermedades(request):
  if request.method=='GET':
    enfermedades = Enfermedades.objects.all()
    enfermedades_serializado = serializers.serialize('json', enfermedades)
    return JsonResponse({"data": enfermedades_serializado}, safe=False)
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
        usuario = idUsuario_instancia,
        pedido = idPedido_instancia,
        platillo = idPlatillo_instancia
      )
      listaCreada.save()
    return JsonResponse({"message": "Lista de pedidos agregada"}, safe=False)
  else:
    return JsonResponse({"message": "Bad request"}, safe=False)
  
####################################################### CRUD DE PEDIDOS ####################################################
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