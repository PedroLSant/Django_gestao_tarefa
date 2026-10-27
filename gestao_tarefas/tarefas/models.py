
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    PRIORIDADE_CHOICES = [
        ("BAIXA", "Baixa"),
        ("MEDIA", "Média"),
        ("ALTA", "Alta"),
    ]

    SITUACAO_CHOICES = [
        ("PENDENTE", "Pendente"),
        ("CONCLUIDA", "Concluída"),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    prioridade = models.CharField(
        max_length=10,
        choices=PRIORIDADE_CHOICES,
        default="MEDIA"
    )
    data_prevista = models.DateField(null=True, blank=True)
    situacao = models.CharField(
        max_length=10,
        choices=SITUACAO_CHOICES,
        default="PENDENTE"
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.titulo
