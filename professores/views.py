from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Professores
from django.db.models import Q, Value
from django.views import View
from django.views.generic.list import ListView
from django.db.models.functions import Concat


class professores (ListView):
    model = Professores
    template_name = 'professores/professores.html'
    paginate_by = 25
    context_object_name = 'professores'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(nome=True)

        return qs

class link_professores (View):
    template_name = 'professores/link_professores.html'
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        pk = self.kwargs.get('professores_id')
        professor = get_object_or_404(Professores, id=pk)
        self.contexto = {
            'professores': professor
        }
        
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

class busca_professores(professores):
    template_name = 'professores/busca_professores.html'
    
    def get_queryset(self):
        termo = self.request.GET.get('termo')
        if termo is None:
            raise Http404()

        campos = Concat('nome', Value(' '), 'sobrenome')

        professores = Professores.objects.annotate(
            nome_completo=campos).filter(
                Q(nome_completo__icontains=termo) |
                Q(id__icontains=termo) |
                Q(especialidade__icontains=termo),
            )

        return professores
