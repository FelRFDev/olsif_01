from rest_framework import viewsets
from django.views.generic import TemplateView
from .models import TerminalLogistico, TrechoFerroviario, Indicador, RegistroDado
from .serializers import (
    TerminalSerializer, TrechoSerializer, 
    IndicadorSerializer, RegistroDadoSerializer
)

# View do Frontend (Dashboard)
class DashboardView(TemplateView):
    template_name = 'logistica/dashboard.html'

# Views da API
class TerminalViewSet(viewsets.ModelViewSet):
    queryset = TerminalLogistico.objects.all()
    serializer_class = TerminalSerializer

class TrechoViewSet(viewsets.ModelViewSet):
    queryset = TrechoFerroviario.objects.all()
    serializer_class = TrechoSerializer

class IndicadorViewSet(viewsets.ModelViewSet):
    queryset = Indicador.objects.all()
    serializer_class = IndicadorSerializer

class RegistroDadoViewSet(viewsets.ModelViewSet):
    queryset = RegistroDado.objects.all().order_by('-data_registro')
    serializer_class = RegistroDadoSerializer
