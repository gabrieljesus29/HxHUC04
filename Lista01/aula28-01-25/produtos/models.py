from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    estoque = models.IntegerField()

    def __str__(self):
        return self.nome
# Create your models here.
