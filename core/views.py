from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Nota
from django.urls import reverse

# Create your views here.
def index(request):
    lista_notas = Nota.objects.order_by('-data_edicao')
    context = {'lista_notas': lista_notas}
    return render(request, 'core/notas.html', context)

def adicionar(request):
    return render(request, 'core/adicionar.html')

def visualizar(request, nota_id):
    try:
        nota = Nota.objects.get(pk=nota_id)
    except Nota.DoesNotExist:
        raise Http404('Nota não existe')
    context = {'nota' : nota}
    return render(request, 'core/visualizar.html', context)

def envianota(request):
    nota = Nota(texto=request.POST['novotexto'])
    nota.save()
    return HttpResponseRedirect(reverse('core:index'))

def editanota(request, nota_id):
    nota = Nota.objects.get(pk=nota_id)
    nota.texto = request.POST['novotexto']
    nota.save()
    return HttpResponseRedirect(reverse('core:index'))

def deletanota(request, nota_id):
    try:
        nota = Nota.objects.get(pk=nota_id)
    except Nota.DoesNotExist:
        raise Http404('Nota não existe')
    nota.delete()
    return HttpResponseRedirect(reverse('core:index'))