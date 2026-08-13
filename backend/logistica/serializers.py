from rest_framework import serializers
from .models import TerminalLogistico, TrechoFerroviario, Indicador, RegistroDado

class TerminalSerializer(serializers.ModelSerializer):
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)
    
    class Meta:
        model = TerminalLogistico
        fields = '__all__'

class TrechoSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = TrechoFerroviario
        fields = '__all__'

class IndicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicador
        fields = '__all__'

class RegistroDadoSerializer(serializers.ModelSerializer):
    indicador_nome = serializers.CharField(source='indicador.nome', read_only=True)
    unidade_medida = serializers.CharField(source='indicador.unidade_medida', read_only=True)
    terminal_nome = serializers.CharField(source='terminal.nome', read_only=True)
    trecho_nome = serializers.CharField(source='trecho.nome', read_only=True)
    
    class Meta:
        model = RegistroDado
        fields = '__all__'
