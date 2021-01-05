from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Nota
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    lista_notas = Nota.objects.order_by('-data_edicao').filter(autor=request.user.username)
    context = {'lista_notas': lista_notas}
    return render(request, 'core/notas.html', context)

#def login(request):
#    return render(request, 'core/login.html')

@login_required
def envialogin(request):
    email = request.POST['inputEmail']
    senha = request.POST['inputSenha']
    user = authenticate(request, username=email, password=senha)
    if user is not None:
        return redirect('core:index')
    else:
        return redirect('core:login')

@login_required
def cadastrar(request):
    return render(request, 'core/cadastrar.html')

@login_required
def enviacadastro(request):
    nome = request.POST['inputNome']
    email = request.POST['inputEmail']
    senha = request.POST['inputSenha']
    user = User.objects.create_user(email, email, senha)
    user.first_name = nome
    user.save()
    return render(request, 'core/login.html')

@login_required
def adicionar(request):
    return render(request, 'core/adicionar.html')

@login_required
def visualizar(request, nota_id):
    try:
        nota = Nota.objects.get(pk=nota_id)
    except Nota.DoesNotExist:
        raise Http404('Nota não existe')
    context = {'nota' : nota}
    return render(request, 'core/visualizar.html', context)

@login_required
def envianota(request):
    nota = Nota(texto=request.POST['novotexto'], autor=request.user.username)
    nota.save()
    return HttpResponseRedirect(reverse('core:index'))

@login_required
def editanota(request, nota_id):
    nota = Nota.objects.get(pk=nota_id)
    nota.texto = request.POST['novotexto']
    nota.save()
    return HttpResponseRedirect(reverse('core:index'))

@login_required
def deletanota(request, nota_id):
    try:
        nota = Nota.objects.get(pk=nota_id)
    except Nota.DoesNotExist:
        raise Http404('Nota não existe')
    nota.delete()
    return HttpResponseRedirect(reverse('core:index'))

@login_required
def sobre(request):
    return render(request, 'core/sobre.html')