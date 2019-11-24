from rest_framework import serializers

from .models import Articulo


class ArticuloSerializer(serializers.Serializer):
    titulo = serializers.CharField(max_length=150)
    contenido = serializers.CharField()
    autores_id = serializers.IntegerField()

    def create(self, validated_data):
        return Articulo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.contenido = validated_data.get('contenido', instance.contenido)
        instance.autores_id = validated_data.get('autores_id', instance.autores_id)

        instance.save()
        return instance
