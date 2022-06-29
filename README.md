README
======



# Meu guia básico de instalação, configuração e criação do Django framework 4.0 e projeto base teste

### Anotações e projeto criados com o conteúdo das aulas práticas do Busertech e:

https://tutorial.djangogirls.org/pt/

https://docs.djangoproject.com/pt-br/4.0/ 

##### Varias anotaçoes foram feitas NO codigo do projeto


###  Instalando e ativando o virtualenv no Ubuntu
```
> mkdir 'nome da pasta do projeto'
> cd 'nome da pasta do prjeto'
> virtualenv django-venv
Comando 'virtualenv' não encontrado, mas poder ser instalado com:

>sudo apt install python3-virtualenv

> sudo apt install python3-virtualenv

>virtualenv django-venv

> source django-venv/bin/activate #ativa maquina virtual (deve aparecer o nome entre parenteses no terminal)
```
ou

`> source ../venv/bin/activate #ativa o ambiente virtual depois de estar dentro da pasta do projeto`

### Instalando dependencias dentro do ambiente virtual
```
>pip freeze # verifica o que está instalado

> pip install Django (instala o django na máquina virtual  criada)


> django-admin #abre todos os comandos do django (vamos utilizar mais o start project)


> django-admin startproject ola_mundo 
```

#### Para executar e abrir no navegador
```
./manage.py runserver
```
> para executar projeto (deve estar dentro da pasta dele)

### Começando a criar estrutura e arquivos
criar um arquivo views.py dentro da pasta principal do projeto, nela será definido as primeiras funções. Exemplo:

```
from django.shortcuts import render

def ola_mundo(request):
    resposta = {'texto': 'tentativa de texto h1'}
    return render(request, 'ola_mundo.html', resposta)
```
> no exemplo acima, um elemento do html foi injetado por meio de uma função definida no arquivo de views

#### dentro de url deve ser passado o caminho para os arquivos de view, importando as bibliotecas path e views

```
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ola_mundo),
```

#### Deverá ser criada então a pasta templates na pasta raiz do projeto. Nela irão os documentos html do projeto. Para que ela seja vista pelo Django, a configuração deve ser feita dentro do arquivo settings.py:

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, './templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
> Talvez o modulo 'os' deverá ser importado.

### A partir daqui, foram importadas algumas pginas html do projeto de buscador da Buser


### Para habilitar a inclusão de css

Dentro de settings.py:

```
# Build paths inside the project like this: BASE_DIR / 'subdir'.
STATIC_DIR = os.path.join(BASE_DIR,"static")
    
# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR,]
```
#### para os arquivos css, deverá ser criada uma pasta STATIC na raiz do projeto e dentro dela uma pasta CSS com os arquivos css. No html, deverá ser incluido no TOPO do arquivo:

```
{% load static %}
```

e os css importados assim no head:
```
<link rel="stylesheet" href="% static 'css/style.css' %}">`
```
### Adicionar um novo app (modulo)

no terminal:

```
./manage.py startapp nome_app
```
#### Ao adicionar um novo app e dentro da views.py dele incluir funções, foi necessário dar visibilidade dessa nova view e suas funções dentro de urls no projeto principal. 

no urls.py:
```
from modulo_viagens import views as viagens_views #tem que renomear o path da view do novo app para não dar conflito com o path do root que já chama 'view'
```
### Configurar admin

No arquivo do admin.py do novo app criado:

```
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```
Depois:
Executar o runserver e no navegador entrar em http://127.0.0.1:8000/admin/, depois criar usuario e senha normalmente

