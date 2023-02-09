from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno
from django.db.models import Q, Value
from django.views import View
from django.views.generic.list import ListView
from django.db.models.functions import Concat


class alunos (ListView):
    model = Aluno
    template_name = 'alunos/alunos.html'
    paginate_by = 25
    context_object_name = 'alunos'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(nome=True)

        return qs

class link_alunos (View):
    template_name = 'alunos/link_alunos.html'
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        pk = self.kwargs.get('alunos_id')
        aluno = get_object_or_404(Aluno, id=pk)
        self.contexto = {
            'alunos': aluno
        }
        
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

class busca_alunos(alunos):
    template_name = 'alunos/busca_alunos.html'
    
    def get_queryset(self):
        termo = self.request.GET.get('termo')
        if termo is None:
            raise Http404()

        campos = Concat('nome', Value(' '), 'sobrenome')

        alunos = Aluno.objects.annotate(
            nome_completo=campos).filter(
                Q(nome_completo__icontains=termo) |
                Q(id__icontains=termo) |
                Q(curso__icontains=termo),
            )

        return alunos

