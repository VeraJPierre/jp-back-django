from rest_framework import serializers
from .models import *

class FotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        fields = ['id','categoria','nombre', 'url']
class CategoriaSerializer(serializers.ModelSerializer):
    fotos = FotosSerializer(many=True)
    class Meta:
        model = Categoria
        fields = ['nombre','fotos']