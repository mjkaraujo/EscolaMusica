from django.urls import path
from . import views

urlpatterns = [
    path('', views.alunos.as_view(), name='alunos'),
    path('busca_alunos/', views.busca_alunos.as_view(), name='busca_alunos'),
    path('link_alunos/<int:alunos_id>', views.link_alunos.as_view(), name='link_alunos'),
]