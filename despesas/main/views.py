from django.shortcuts import render, redirect
from .forms import SaidaForm, EntradaForm, NotaForm, FiltroForm
from .models import Entrada, Saida, Nota
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth import logout as django_logout


def index(request, id):
    return render(request, 'main/index.html', {'id': id})

from django.shortcuts import render, redirect
from .forms import SaidaForm, EntradaForm
from .models import Entrada, Saida
from django.contrib.auth.decorators import login_required

@login_required
def entradas(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            entrada = form.save(commit=False)
            entrada.user = request.user
            entrada.save()
            return redirect('entradas')  # Redirecione para a página de entradas após o salvamento
    else:
        form = EntradaForm()

    entradas_salvas = Entrada.objects.filter(user=request.user)
    return render(request, 'main/entradas.html', {'form': form, 'entradas_salvas': entradas_salvas})

@login_required
def saidas(request):
    if request.method == 'POST':
        form = SaidaForm(request.POST)
        if form.is_valid():
            saida = form.save(commit=False)
            saida.user = request.user
            saida.save()
            return redirect('saidas')  # Redirecione para a página de saídas após o salvamento
    else:
        form = SaidaForm()

    saidas_salvas = Saida.objects.filter(user=request.user)
    return render(request, 'main/saidas.html', {'form': form, 'saidas_salvas': saidas_salvas})

@login_required
def view(request):
    # Obter entradas e saídas ordenadas por data
    entradas = Entrada.objects.filter(user=request.user).order_by('data')
    saidas = Saida.objects.filter(user=request.user).order_by('data')

    # Calcular os totais
    total_entradas = sum(entrada.valor for entrada in entradas)
    total_saidas = sum(saida.valor for saida in saidas)

    return render(request, 'main/view.html', {
        'entradas': entradas,
        'saidas': saidas,
        'total_entradas': total_entradas,
        'total_saidas': total_saidas,
    })

@login_required
def notas(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.user = request.user
            nota.save()
            return redirect('notas')  # Redirecione para a página de notas
    else:
        form = NotaForm()

    notas = Nota.objects.filter(user=request.user).order_by('-data_criacao')

    return render(request, 'main/home.html', {'form': form, 'notas': notas})

def paginainicial(request):
    return render(request, "main/paginainicial.html")


@login_required
def view(request):
    filtro_form = FiltroForm(request.GET)

    if filtro_form.is_valid():
        mes = filtro_form.cleaned_data['mes']
        ano = filtro_form.cleaned_data['ano']
        entradas = Entrada.objects.filter(user=request.user, data__month=mes, data__year=ano)
        saidas = Saida.objects.filter(user=request.user, data__month=mes, data__year=ano)
        total_entradas = entradas.aggregate(total_entradas=models.Sum('valor'))['total_entradas'] or 0
        total_saidas = saidas.aggregate(total_saidas=models.Sum('valor'))['total_saidas'] or 0
    else:
        entradas = Entrada.objects.filter(user=request.user)
        saidas = Saida.objects.filter(user=request.user)
        total_entradas = entradas.aggregate(total_entradas=models.Sum('valor'))['total_entradas'] or 0
        total_saidas = saidas.aggregate(total_saidas=models.Sum('valor'))['total_saidas'] or 0

    return render(request, 'main/view.html', {'entradas': entradas, 'saidas': saidas, 'total_entradas': total_entradas, 'total_saidas': total_saidas, 'filtro_form': filtro_form})
    
def logout(request):
    if request.method == 'POST' or request.method == 'GET':
        # Ações de logout
        django_logout(request)
        return redirect('login')

