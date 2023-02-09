from django.urls import path
from . import views

urlpatterns = [
    path('fotos/', views.FotosIndex.as_view(), name='fotos'),
    path('albuns/<str:albuns>', views.FotosAlbuns.as_view(), name='albuns'),
    path('busca/', views.FotosBusca.as_view(), name='fotos_busca'),
    path('fotos/<slug:pk>', views.FotosDetalhes.as_view(), name='fotos_detalhes'),
]