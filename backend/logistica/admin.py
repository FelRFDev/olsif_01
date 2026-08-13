from django.contrib import admin
from .models import TerminalLogistico, TrechoFerroviario, Indicador, RegistroDado

@admin.register(TerminalLogistico)
class TerminalLogisticoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'latitude', 'longitude')
    list_filter = ('tipo',)
    search_fields = ('nome',)

@admin.register(TrechoFerroviario)
class TrechoFerroviarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'origem', 'destino', 'distancia_km', 'status')
    list_filter = ('status',)
    search_fields = ('nome', 'origem', 'destino')

@admin.register(Indicador)
class IndicadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'unidade_medida')
    search_fields = ('nome',)

@admin.register(RegistroDado)
class RegistroDadoAdmin(admin.ModelAdmin):
    list_display = ('indicador', 'valor', 'data_registro', 'terminal', 'trecho')
    list_filter = ('data_registro', 'indicador')
    date_hierarchy = 'data_registro'
