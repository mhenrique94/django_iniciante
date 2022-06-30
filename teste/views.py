from django.shortcuts import render

def pag_principal(request):
    return render(request, 'buscador.html')

def pag_viagens(request):
    return render(request, 'viagens.html')