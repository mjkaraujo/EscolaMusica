from django.urls import path
from . import views

urlpatterns = [
    path('', views.mensalidades.as_view(), name='mensalidades'),
    path('busca_mensalidades/', views.busca_mensalidades.as_view(), name='busca_mensalidades'),
    path('link_mensalidades/<int:mensalidades_id>', views.link_mensalidades.as_view(), name='link_mensalidades'),
]