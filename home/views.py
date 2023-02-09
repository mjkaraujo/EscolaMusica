from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from home.forms import FormContatos
from cursos.forms import FormCursos
from alunos.forms import FormAlunos
from mensalidades.forms import FormMensalidade
from professores.forms import FormProfessores
from django.core.paginator import Paginator
from alunos.models import Aluno
from professores.models import Professores
from mensalidades.models import Mensalidade

from django.http import Http404
from django.db.models import Q
from django.core.validators import validate_email


def index(request):
    return render (request, 'home/index.html')

def blog(request):
    return render (request, 'posts/blog.html')

def quemSomos(request):
    return render (request, 'home/quemSomos.html')

def metodologia(request):
    return render (request, 'home/metodologia.html')
    
def guitarra(request):
    if str(request.method) == 'POST':
        form = FormCursos(request.POST or None)
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Sua mensagem foi enviada com sucesso!')
            form = FormCursos()
        else:
            messages.error(request, 'Não foi possível enviar o seu email.') 
    else:
        form = FormCursos()
    context = {
        'form':form
    }
    return render (request, 'cursos/guitarra.html', context)

def violao(request):
    if str(request.method) == 'POST':
        form = FormCursos(request.POST or None)
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Sua mensagem foi enviada com sucesso!')
            form = FormCursos()
        else:
            messages.error(request, 'Não foi possível enviar o seu email.') 
    else:
        form = FormCursos()
    context = {
        'form':form
    }
    return render (request, 'cursos/violao.html', context)

def baixo(request):
    if str(request.method) == 'POST':
        form = FormCursos(request.POST or None)
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Sua mensagem foi enviada com sucesso!')
            form = FormCursos()
        else:
            messages.error(request, 'Não foi possível enviar o seu email.') 
    else:
        form = FormCursos()
    context = {
        'form':form
    }
    return render (request, 'cursos/baixo.html', context)
    
def teclado(request):
    if str(request.method) == 'POST':
        form = FormCursos(request.POST or None)
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Sua mensagem foi enviada com sucesso!')
            form = FormCursos()
        else:
            messages.error(request, 'Não foi possível enviar o seu email.') 
    else:
        form = FormCursos()
    context = {
        'form':form
    }
    return render (request, 'cursos/teclado.html', context)

def bateria(request):
    if str(request.method) == 'POST':
        form = FormCursos(request.POST or None)
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Sua mensagem foi enviada com sucesso!')
            form = FormCursos()
        else:
            messages.error(request, 'Não foi possível enviar o seu email.') 
    else:
        form = FormCursos()
    context = {
        'form':form
    }
    return render (request, 'cursos/bateria.html', context)

def canto(request):
    if str(request.method) == 'POST':
        form = FormCursos(request.POST or None)
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Sua mensagem foi enviada com sucesso!')
            form = FormCursos()
        else:
            messages.error(request, 'Não foi possível enviar o seu email.') 
    else:
        form = FormCursos()
    context = {
        'form':form
    }
    return render (request, 'cursos/canto.html', context)

def teoria(request):
    if str(request.method) == 'POST':
        form = FormCursos(request.POST or None)
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Sua mensagem foi enviada com sucesso!')
            form = FormCursos()
        else:
            messages.error(request, 'Não foi possível enviar o seu email.') 
    else:
        form = FormCursos()
    context = {
        'form':form
    }
    return render (request, 'cursos/teoria.html', context)

def harmonia(request):
    if str(request.method) == 'POST':
        form = FormCursos(request.POST or None)
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Sua mensagem foi enviada com sucesso!')
            form = FormCursos()
        else:
            messages.error(request, 'Não foi possível enviar o seu email.') 
    else:
        form = FormCursos()
    context = {
        'form':form
    }
    return render (request, 'cursos/harmonia.html', context)

def percepcao(request):
    if str(request.method) == 'POST':
        form = FormCursos(request.POST or None)
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Sua mensagem foi enviada com sucesso!')
            form = FormCursos()
        else:
            messages.error(request, 'Não foi possível enviar o seu email.') 
    else:
        form = FormCursos()
    context = {
        'form':form
    }
    return render (request, 'cursos/percepcao.html', context)
    

def contatos(request):
    if str(request.method) == 'POST':
        form = FormContatos(request.POST or None)
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Sua mensagem foi enviada com sucesso!')
            form = FormContatos()
        else:
            messages.error(request, 'Não foi possível enviar o seu email.') 
    else:
        form = FormContatos()
    context = {
        'form':form
    }    

    return render(request, 'home/contatos.html', context)

def fotos(request):
    return render (request, 'fotos/fotos.html')

def faq(request):   
    return render (request, 'home/faq.html')


@login_required(redirect_field_name ='login')
def menu_administrativo(request):   
    return render (request, 'administrativa/menu_administrativo.html')

@login_required
def alunos (request):
    alunos = Aluno.objects.order_by('id').filter (
        ocultar = False
    )
    paginator = Paginator(alunos, 20)

    page = request.GET.get('p')
    alunos = paginator.get_page(page)
    
    return render(request, 'alunos/alunos.html', {
        'alunos': alunos
    })

@login_required
def link_alunos (request):
    return render(request, 'alunos/link_alunos.html')

@login_required
def busca_alunos (request):
    return render(request, 'alunos/busca_alunos.html')

@login_required
def cadastro_alunos (request, **kwargs):
    if request.method != 'POST':
        form = FormAlunos()
        return render(request, 'alunos/cadastro_alunos.html', {  
            'form': form})
    form = FormAlunos(request.POST, request.FILES)
  
    if not form.is_valid():
        messages.error(request, 'Erro ao enviar os dados!')    
        form = FormAlunos()
        return render(request, 'alunos/alunos.html', {  
            'form': form})
    
    form.save()
    messages.success(request, f'Aluno {request.POST.get("nome")} cadastrado com sucesso!')
    return redirect('alunos')

@login_required
def professores (request):
    professores = Professores.objects.order_by('id').filter (
        ocultar = False
    )
    paginator = Paginator(professores, 20)

    page = request.GET.get('p')
    professores = paginator.get_page(page)
    
    return render(request, 'professores/professores.html', {
        'professores': professores
    })

@login_required
def link_professores (request):
    return render(request, 'professores/link_professores.html')

@login_required
def busca_professores (request):
    return render(request, 'professores/busca_professores.html')

@login_required
def cadastro_professores (request, **kwargs):
    if request.method != 'POST':
        form = FormProfessores()
        return render(request, 'professores/cadastro_professores.html', {  
            'form': form})
    form = FormProfessores(request.POST, request.FILES)
  
    if not form.is_valid():
        messages.error(request, 'Erro ao enviar os dados!')    
        form = FormProfessores()
        return render(request, 'professores/professores.html', {  
            'form': form})
    
    form.save()
    messages.success(request, f'Professor {request.POST.get("nome")} cadastrado com sucesso!')
    return redirect('professores')

@login_required
def mensalidades (request):
    mensalidades = Mensalidade.objects.order_by('id').filter (
        ocultar = False
    )
    paginator = Paginator(mensalidades, 20)

    page = request.GET.get('p')
    mensalidades = paginator.get_page(page)
    
    return render(request, 'mensalidades/mensalidades.html', {
        'mensalidades': mensalidades
    })

@login_required
def cadastro_mensalidades (request, **kwargs):
    if request.method != 'POST':
        form = FormMensalidade()
        return render(request, 'mensalidades/cadastro_mensalidades.html', {  
            'form': form})
    form = FormMensalidade(request.POST, request.FILES)
  
    if not form.is_valid():
        messages.error(request, 'Erro ao enviar os dados!')    
        form = FormMensalidade()
        return render(request, 'mensalidades/mensalidades.html', {  
            'form': form})
    
    form.save()
    messages.success(request, f'Mensalidade do Aluno {request.POST.get("aluno")} cadastrado com sucesso!')
    return redirect('mensalidades')

@login_required
def link_mensalidades (request):
    return render(request, 'mensalidades/link_mensalidades.html')

@login_required
def busca_mensalidades (request):
    return render(request, 'mensalidades/busca_mensalidades.html')

@login_required
def logout (request):
    auth.logout(request)
    return redirect('login')