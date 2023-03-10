from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.index, name='blog'),
    path('quemSomos/', views.quemSomos, name='quemSomos'),
    path('metodologia/', views.metodologia, name='metodologia'),
    path('guitarra/', views.guitarra, name='guitarra'),
    path('violao/', views.violao, name='violao'),
    path('baixo/', views.baixo, name='baixo'),
    path('teclado/', views.teclado, name='teclado'),
    path('bateria/', views.bateria, name='bateria'),
    path('canto/', views.canto, name='canto'),
    path('teoria/', views.teoria, name='teoria'),
    path('harmonia/', views.harmonia, name='harmonia'),
    path('percepcao/', views.percepcao, name='percepcao'),
    path('contatos/', views.contatos, name='contatos'),
    path('fotos/', views.fotos, name='fotos'),
    path('faq/', views.faq, name='faq'),
    path('administrativa/', views.menu_administrativo, name='menu_administrativo'),
    path('logout/', views.logout, name='logout'),
    path('alunos/',views.alunos, name='alunos'),
    path('busca_alunos/<int:alunos_id>', views.busca_alunos, name='busca_alunos'),
    path('link_alunos/<int:alunos_id>', views.link_alunos, name='link_alunos'),
    path('cadastro_alunos/', views.cadastro_alunos, name='cadastro_alunos'),
    path('professores/',views.professores, name='professores'),
    path('busca_professores/<int:professores_id>', views.busca_professores, name='busca_professores'),
    path('link_professores/<int:professores_id>', views.link_professores, name='link_professores'),
    path('cadastro_professores/', views.cadastro_professores, name='cadastro_professores'),
    path('mensalidades/', views.mensalidades, name='mensalidades'),
    path('cadastro_mensalidades/', views.cadastro_mensalidades, name='cadastro_mensalidades'),
    path('busca_mensalidades/<int:mensalidades_id>', views.busca_mensalidades, name='busca_mensalidades'),
]