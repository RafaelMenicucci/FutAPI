from django.db import models


class Jogos(models.Model):
    time_casa = models.CharField(max_length=30)
    time_fora = models.CharField(max_length=30)
    gols_casa = models.IntegerField()
    gols_fora = models.IntegerField()
    ano = models.IntegerField()
    rodada = models.IntegerField()
    amarelo_casa = models.IntegerField()
    amarelo_fora = models.IntegerField()
    vermelho_casa = models.IntegerField()
    vermelho_fora = models.IntegerField()
    escanteio_casa = models.IntegerField()
    escanteio_fora = models.IntegerField()
    faltas_casa = models.IntegerField()
    faltas_fora = models.IntegerField()
    chutes_casa = models.IntegerField()
    chutes_fora = models.IntegerField()
    defesa_casa = models.IntegerField()
    defesa_fora = models.IntegerField()

    def __str__(self):
        return (
            self.ano
            + " - "
            + self.rodada
            + " - "
            + self.time_casa
            + " X "
            + self.time_fora
        )
