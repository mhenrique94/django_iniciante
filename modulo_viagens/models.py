from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): 
    """ isso define que é um objeto e 'models.Model' que é um modelo de django, que será salvo no banco de dados 
    Sempre inicie o nome de uma classe com uma letra em maiúsculo.
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #relação com outro modelo
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

"""
    após criação de um modelo, ele deverá ser adicionado ao banco de dados por meio do migrations.
    
    no console digitar ./manage.py makemigrations nome_app
    
"""