from django.db import models

# Create your models here.


class Autor(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()


class Articulo(models.Model):
    autores = models.ForeignKey('Autor', related_name='articulos', on_delete=models.PROTECT)
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo
