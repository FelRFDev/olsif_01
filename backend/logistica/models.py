from django.db import models

class TerminalLogistico(models.Model):
    TIPO_CHOICES = (
        ('porto_seco', 'Porto Seco'),
        ('patio', 'Pátio Ferroviário'),
        ('transbordo', 'Área de Transbordo'),
        ('outro', 'Outro'),
    )
    nome = models.CharField(max_length=150)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    capacidade = models.CharField(max_length=150, blank=True, null=True, help_text='Ex: 500 TEUs/dia')
    
    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"

class TrechoFerroviario(models.Model):
    STATUS_CHOICES = (
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo/Sucateado'),
        ('manutencao', 'Em Manutenção'),
    )
    nome = models.CharField(max_length=150, help_text='Ex: Uruguaiana - Cacequi')
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    distancia_km = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativo')

    def __str__(self):
        return self.nome

class Indicador(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    unidade_medida = models.CharField(max_length=50, help_text='Ex: Toneladas, R$/TKU')

    def __str__(self):
        return self.nome

class RegistroDado(models.Model):
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE, related_name='registros')
    terminal = models.ForeignKey(TerminalLogistico, on_delete=models.SET_NULL, null=True, blank=True)
    trecho = models.ForeignKey(TrechoFerroviario, on_delete=models.SET_NULL, null=True, blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    data_registro = models.DateField()
    
    def __str__(self):
        return f"{self.indicador.nome}: {self.valor} em {self.data_registro}"
