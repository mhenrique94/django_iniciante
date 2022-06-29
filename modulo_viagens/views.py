from django.shortcuts import render

def pag_viagens(request):
    return render(request, 'viagens.html')
