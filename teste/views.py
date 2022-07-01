from django.shortcuts import render
from django.utils import timezone
from teste.models import Post

def pag_principal(request):
    return render(request, 'buscador.html')


def pag_viagens(request): 
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'viagens.html', {'posts': posts})