from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)  # novo campo nome
    idade = models.IntegerField()
    salario_mensal = models.FloatField()
    score_credito = models.FloatField()
    tempo_emprego_anos = models.FloatField()
    estado_civil = models.CharField(max_length=20)
    possui_imovel = models.BooleanField()
    possui_veiculo = models.BooleanField()
    qtd_cartoes_credito = models.IntegerField()
    historico_inadimplencia = models.BooleanField()
    valor_credito_solicitado = models.FloatField()
    dividas_banco_A = models.FloatField()
    dividas_banco_B = models.FloatField()
    dividas_banco_C = models.FloatField()
    dividas_totais = models.FloatField()

    # Campos que serão preenchidos após análise
    score_risco = models.FloatField(null=True, blank=True)
    aprovado_previsto = models.BooleanField(null=True, blank=True)
    data_analise = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.nome} (ID {self.id}) - Score: {self.score_risco:.2f}" if self.score_risco else f"{self.nome} (ID {self.id})"
