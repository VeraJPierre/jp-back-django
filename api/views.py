from django.http import HttpResponse
from .models import *
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes


# Create your views here.
def index(request):
  return HttpResponse('<h1>Hola Codigo</h1>')




class CategoriasList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# con retrieve, update ahcemos el put push  y destroy borrar
class CategoriasGet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class FotosList(generics.ListCreateAPIView):
    queryset = Foto.objects.all()
    serializer_class = FotosSerializer

# con retrieve, update ahcemos el put push  y destroy borrar
class FotosGet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Foto.objects.all()
    serializer_class = FotosSerializer
# Create your views here.
