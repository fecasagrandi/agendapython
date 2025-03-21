from django.db import models

class Contato (models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=18)

    def __str__(self):
        return f'{self.nome}'
    
