from django.contrib import admin

# Register your models here.

from .models import Articulo, Autor

admin.site.register(Articulo)
admin.site.register(Autor)
