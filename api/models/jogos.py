from django.db import models


class Jogos(models.Model):
    ano = models.IntegerField()
    rodada = models.IntegerField()
    time_casa = models.CharField(max_length=30)
    time_fora = models.CharField(max_length=30)
    gols_casa = models.IntegerField(blank=True, null=True)
    gols_fora = models.IntegerField(blank=True, null=True)
    chutes_casa = models.IntegerField(blank=True, null=True)
    chutes_fora = models.IntegerField(blank=True, null=True)
    defesa_casa = models.IntegerField(blank=True, null=True)
    defesa_fora = models.IntegerField(blank=True, null=True)
    escanteio_casa = models.IntegerField(blank=True, null=True)
    escanteio_fora = models.IntegerField(blank=True, null=True)
    faltas_casa = models.IntegerField(blank=True, null=True)
    faltas_fora = models.IntegerField(blank=True, null=True)
    amarelo_casa = models.IntegerField(blank=True, null=True)
    amarelo_fora = models.IntegerField(blank=True, null=True)
    vermelho_casa = models.IntegerField(blank=True, null=True)
    vermelho_fora = models.IntegerField(blank=True, null=True)

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
