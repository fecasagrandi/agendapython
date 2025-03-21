from django.urls import path
from .views import inserirContato, listarContatos, atualizarContato, deletarContato

urlpatterns = [
    path('nova/', inserirContato, name="inserirContato"),
    path("listar/", listarContatos, name="listarContatos"),
    path("atualizar/<int:pk>/", atualizarContato, name="atualizarContato"),
    path("deletar/<int:pk>/", deletarContato, name="deletarContato"),
]
