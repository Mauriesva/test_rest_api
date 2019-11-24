from django.shortcuts import get_object_or_404

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Articulo
from .serializers import ArticuloSerializer


class ArticuloView(APIView):
    def get(self, request):
        articulos = Articulo.objects.all()
        serializer = ArticuloSerializer(articulos, many=True)
        return Response({"articulos": serializer.data})

    def post(self, request):
        articulo = request.data.get('articulo')

        serializer = ArticuloSerializer(data=articulo)
        if serializer.is_valid(raise_exception=True):
            articulo_creado = serializer.save()
        return Response({"exito": "Articulo '{}' creaado satisfactoriamente".format(articulo_creado.titulo)})

    def put(self, request, pk):
        articulo_actualizado = get_object_or_404(Articulo.objects.all(), pk=pk)
        data = request.data.get('articulo')
        serializer = ArticuloSerializer(instance=articulo_actualizado, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            articulo_actualizado = serializer.save()
        return Response({"exito": "Articulo '{}' actualizado satisfactoriamente".format(articulo_actualizado.titulo)})

    def delete(self, request, pk):
        article = get_object_or_404(Articulo.objects.all(), pk=pk)
        article.delete()
        return Response({"mensaje": "Articulo con id `{}` ha sido eliminado.".format(pk)},status=204)
