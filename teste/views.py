from django.shortcuts import render

def pag_principal(request):
    return render(request, 'index.html')

