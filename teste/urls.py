"""teste URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from teste import views

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls, name='adminpanel'),
    path('', views.pag_principal, name='index'),
    path('viagens/', views.pag_viagens, name='viagens'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('contato/', views.contact_view, name='contato'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name="cadastrar_usuario"),
    path('logar_usuario', views.logar_usuario, name="logar_usuario"),
    path('deslogar_usuario', views.deslogar_usuario, name="deslogar_usuario"),
    path('alterar_senha/', views.alterar_senha, name='alterar_senha'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
