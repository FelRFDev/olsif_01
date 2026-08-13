from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DashboardView,
    TerminalViewSet, TrechoViewSet, 
    IndicadorViewSet, RegistroDadoViewSet
)

router = DefaultRouter()
router.register(r'terminais', TerminalViewSet)
router.register(r'trechos', TrechoViewSet)
router.register(r'indicadores', IndicadorViewSet)
router.register(r'registros', RegistroDadoViewSet)

urlpatterns = [
    # Rota principal do Dashboard Frontend
    path('', DashboardView.as_view(), name='dashboard'),
    
    # Rotas da API
    path('api/', include(router.urls)),
]
