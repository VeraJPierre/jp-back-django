from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Foto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='fotos')
    nombre = models.CharField(max_length=200)
    url = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.nombre