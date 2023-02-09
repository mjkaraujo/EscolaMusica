from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostIndex.as_view(), name='blog'),
    path('categorias/<str:categorias>', views.PostCategoria.as_view(), name='post_categoria'),
    path('busca/', views.PostBusca.as_view(), name='post_busca'),
    path('post/<slug:pk>', views.PostDetalhes.as_view(), name='post_detalhes'),
]