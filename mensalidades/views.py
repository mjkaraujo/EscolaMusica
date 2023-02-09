from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Mensalidade
from django.db.models import Q, Value, FloatField
from django.views import View
from django.views.generic.list import ListView
from django.db.models.functions import Concat


class mensalidades (ListView):
    model = Mensalidade
    template_name = 'mensalidades/mensalidades.html'
    paginate_by = 25
    context_object_name = 'mensalidades'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(status=True)

        return qs

class link_mensalidades (View):
    template_name = 'mensalidades/link_mensalidades.html'
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        pk = self.kwargs.get('mensalidades_id')
        mensalidade = get_object_or_404(Mensalidade, id=pk)
        self.contexto = {
            'mensalidades': mensalidade
        }
        
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

class busca_mensalidades(mensalidades):
    template_name = 'mensalidades/busca_mensalidades.html'
    
    def get_queryset(self):
        termo = self.request.GET.get('termo')
        if termo is None:
            raise Http404()

        mensalidades = Mensalidade.objects.filter(
                Q(id__icontains=termo) |
                Q(vencimento__icontains=termo) |
                Q(status__icontains=termo),
            )

        return mensalidades
