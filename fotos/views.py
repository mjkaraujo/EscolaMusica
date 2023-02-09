from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from .models import Fotos
from django.db.models import Q, Count, Case, When
from django.views import View

class FotosIndex(ListView):
    model = Fotos
    template_name = 'fotos/fotos.html'
    paginate_by = 6
    context_object_name = 'fotos'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('albuns_fotos')
        qs = qs.order_by('-id').filter(publicado_fotos=True)

        return qs

class FotosBusca(FotosIndex):
    template_name = 'fotos/busca.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')

        if not termo:
            return qs

        qs = qs.filter(
            Q(titulo_fotos__icontains=termo) |
            Q(autor_fotos__first_name__iexact=termo) |
            Q(conteudo_fotos__icontains=termo) |
            Q(excerto_fotos__icontains=termo) |
            Q(albuns_fotos__nome_albuns__iexact=termo)
        )

        return qs

class FotosAlbuns(FotosIndex):
    template_name = 'fotos/albuns.html'

    def get_queryset(self):
        qs = super().get_queryset()

        albuns = self.kwargs.get('albuns', None)

        if not albuns:
            return qs

        qs = qs.filter(albuns_fotos__nome_albuns__iexact=albuns)

        return qs

class FotosDetalhes(View):
    template_name = 'fotos/fotos_detalhes.html'
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        pk = self.kwargs.get('pk')
        fotos = get_object_or_404(Fotos, pk=pk, publicado_fotos=True)
        self.contexto = {
            'fotos': fotos,
        }
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)