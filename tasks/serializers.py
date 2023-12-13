from rest_framework import serializers
from .models import Enfermedades, Intolerancias, Necesidades, Preferencias, ListaEnfermedades, ListaIntolerancias, ListaNecesidades, ListaPreferencias, Usuario

class EnfermedadSerializer(serializers.ModelSerializer):
  class Meta:
      model = Enfermedades
      fields = '__all__'

class IntoleranciasSerializer(serializers.ModelSerializer):
  class Meta:
      model = Intolerancias
      fields = '__all__'

class NecesidadesSerializer(serializers.ModelSerializer):
  class Meta:
      model = Necesidades
      fields = '__all__'

class PreferenciasSerializer(serializers.ModelSerializer):
  class Meta:
      model = Preferencias
      fields = '__all__'

class ListaEnfermedadesSerializer(serializers.ModelSerializer):
  enfermedades = EnfermedadSerializer(many=True, read_only=True)

  class Meta:
      model = ListaEnfermedades
      fields = '__all__'

class ListaIntoleranciasSerializer(serializers.ModelSerializer):
  intolerancias = IntoleranciasSerializer(many=True, read_only=True)

  class Meta:
      model = ListaIntolerancias
      fields = '__all__'

class ListaNecesidadesSerializer(serializers.ModelSerializer):
  necesidades = NecesidadesSerializer(many=True, read_only=True)

  class Meta:
      model = ListaNecesidades
      fields = '__all__'

class ListaPreferenciasSerializer(serializers.ModelSerializer):
  preferencias = PreferenciasSerializer(many=True, read_only=True)

  class Meta:
      model = ListaPreferencias
      fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
  lista_preferencias = ListaPreferenciasSerializer(many=True, read_only=True)
  lista_enfermedades = ListaEnfermedadesSerializer(many=True, read_only=True)
  lista_necesidades = ListaNecesidadesSerializer(many=True, read_only=True)
  lista_intolerancias = ListaIntoleranciasSerializer(many=True, read_only=True)

  class Meta:
    model = Usuario
    fields = '__all__'
