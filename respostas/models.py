from django.db import models
from perguntas.models import Pergunta

class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete = models.CASCADE)
    resp_texto = models.TextField("Resposta")

    class Meta:
        db_table = "respostas"

    def __str__(self):
        return self.pergunta.titulo + "  " + self.resp_texto
