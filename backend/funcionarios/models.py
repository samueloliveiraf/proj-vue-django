from django.db import models


class Funcionario(models.Model):
    nome = models.CharField(max_length=1024, blank=True, null=True)
    cargo = models.CharField(max_length=1024, blank=True, null=True)
    idade = models.IntegerField()
    ativo = models.BooleanField(default=True)
    data = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Funcionarios'
        verbose_name = 'Funcionario'
        db_table = 'funcionarios'
        ordering = ['-id']
