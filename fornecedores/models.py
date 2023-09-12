from django.db import models




class Fornecedores(models.Model):
    nome = models.TextField(max_length=40, null=False, blank=False, default=None)
    produto_e_servicos = models.TextField(max_length=40, null=False, blank=False, default=None)
    telefone = models.TextField(max_length=11, null=False, blank=False, default=None)
    email = models.TextField(max_length=50, null=False, blank=False, default=None)
    
    def __str__(self):
        return self.nome
