from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from teste.forms import ContactForm
from teste.models import Post

def pag_principal(request):
    return render(request, 'buscador.html')


def pag_viagens(request): 
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'viagens.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'sucesso.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contato.html', context)