from django.db import models

class Pergunta(models.Model):
    TIPOS_PERGUNTAS = (
        ('estrelas','Estrelas'),
        ('sim/não','Sim/Não'),
        ('subjetivo','Subjetivo'),
    )
    titulo = models.TextField(
        'Pergunta',
    )
    tipo_pergunta = models.CharField(
        'Tipo de pergunta',
        max_length = 10,
        choices = TIPOS_PERGUNTAS,
    )
    ativo = models.BooleanField('Campo Ativo',default=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "perguntas"

    def __str__(self):
        return self.titulo + " " + self.tipo_pergunta

    def e_estrela(self):
        if self.tipo_pergunta == "estrelas":
            return True
        else:
            return False

    def e_sim_nao(self):
        if self.tipo_pergunta == "sim/não":
            return True
        else:
            return False

    def e_subjetivo(self):
        if self.tipo_pergunta == "subjetivo":
            return True
        else:
            return False
