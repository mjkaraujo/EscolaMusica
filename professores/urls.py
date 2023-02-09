from django.urls import path
from . import views

urlpatterns = [
    path('', views.professores.as_view(), name='professores'),
    path('busca_professores/', views.busca_professores.as_view(), name='busca_professores'),
    path('link_professores/<int:professores_id>', views.link_professores.as_view(), name='link_professores'),
]