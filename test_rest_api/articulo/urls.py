from django.urls import path

from .views import ArticuloView


app_name = "articulos"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articulos/', ArticuloView.as_view()),
    path('articulos/<int:pk>', ArticuloView.as_view())
]
