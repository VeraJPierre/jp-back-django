from django.urls import path
from api import views
urlpatterns = [
    path('', views.index),
    path('categoriasList/', views.CategoriasList.as_view()),
    path('categoriasList/<str:pk>', views.CategoriasGet.as_view()),
    path('subcategoriasList/', views.FotosList.as_view()),
    path('subcategoriasList/<int:pk>', views.FotosGet.as_view()),
]