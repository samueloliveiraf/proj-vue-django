from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=1024, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    data = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Produtos'
        verbose_name = 'Produto'
        db_table = 'produtos'
        ordering = ['-id']
