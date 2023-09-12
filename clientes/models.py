from django.db import models



class Clientes(models.Model):
    apelido = models.TextField(max_length=20, null=False, blank=False, default=None)
    nome = models.TextField(max_length=40, null=False, blank=False, default=None)
    telefone = models.TextField(max_length=11, null=False, blank=False, default=None)
    email = models.TextField(max_length=50, null=False, blank=False, default=None)
    
    def __str__(self):
        return self.nome

