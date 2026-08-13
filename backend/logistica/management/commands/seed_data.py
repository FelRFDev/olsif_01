import random
from datetime import timedelta, date
from django.core.management.base import BaseCommand
from logistica.models import TerminalLogistico, TrechoFerroviario, Indicador, RegistroDado

class Command(BaseCommand):
    help = 'Gera dados fictícios (mockados) para popular o banco de dados do OLSIF'

    def handle(self, *args, **kwargs):
        self.stdout.write('Iniciando a geração de dados mockados...')

        # Limpar dados antigos
        RegistroDado.objects.all().delete()
        TrechoFerroviario.objects.all().delete()
        TerminalLogistico.objects.all().delete()
        Indicador.objects.all().delete()

        # 1. Criar Terminais (Foco na região Sul / Mercosul)
        terminais_data = [
            {'nome': 'Porto Seco Rodoviário de Uruguaiana', 'tipo': 'porto_seco', 'lat': -29.754, 'lng': -57.081, 'cap': '600 Caminhões/dia'},
            {'nome': 'Pátio Ferroviário de Uruguaiana', 'tipo': 'patio', 'lat': -29.761, 'lng': -57.090, 'cap': '3000 Ton/dia'},
            {'nome': 'Pátio de Cacequi', 'tipo': 'patio', 'lat': -29.883, 'lng': -54.825, 'cap': 'Entroncamento - 5000 Ton/dia'},
            {'nome': 'Porto de Rio Grande', 'tipo': 'transbordo', 'lat': -32.122, 'lng': -52.100, 'cap': '50000 TEUs/mês'},
            {'nome': 'Paso de los Libres (ARG)', 'tipo': 'porto_seco', 'lat': -29.712, 'lng': -57.085, 'cap': 'Fronteira'},
        ]
        
        terminais = []
        for t in terminais_data:
            term = TerminalLogistico.objects.create(
                nome=t['nome'], tipo=t['tipo'], 
                latitude=t['lat'], longitude=t['lng'], capacidade=t['cap']
            )
            terminais.append(term)
        self.stdout.write(self.style.SUCCESS(f'{len(terminais)} terminais criados.'))

        # 2. Criar Trechos
        trechos_data = [
            {'nome': 'Uruguaiana - Cacequi', 'origem': 'Uruguaiana', 'destino': 'Cacequi', 'dist': 350.5, 'status': 'ativo'},
            {'nome': 'Cacequi - Rio Grande', 'origem': 'Cacequi', 'destino': 'Rio Grande', 'dist': 420.0, 'status': 'ativo'},
            {'nome': 'Uruguaiana - Alegrete', 'origem': 'Uruguaiana', 'destino': 'Alegrete', 'dist': 140.2, 'status': 'manutencao'},
        ]
        
        trechos = []
        for tr in trechos_data:
            trecho = TrechoFerroviario.objects.create(
                nome=tr['nome'], origem=tr['origem'], destino=tr['destino'],
                distancia_km=tr['dist'], status=tr['status']
            )
            trechos.append(trecho)
        self.stdout.write(self.style.SUCCESS(f'{len(trechos)} trechos criados.'))

        # 3. Criar Indicadores
        ind_volume = Indicador.objects.create(nome='Volume Transportado', descricao='Total de carga movimentada', unidade_medida='Toneladas (Ton)')
        ind_emissao = Indicador.objects.create(nome='Emissões CO2 Evitadas', descricao='Comparativo rodoviário x ferroviário', unidade_medida='Ton CO2')
        ind_custo = Indicador.objects.create(nome='Custo Médio de Frete', descricao='Custo estimado por TKU', unidade_medida='R$/TKU')

        self.stdout.write(self.style.SUCCESS('Indicadores criados.'))

        # 4. Criar Registros Históricos (Séries temporais para os gráficos)
        hoje = date.today()
        registros_criados = 0

        # Gerar 30 dias de dados fictícios para o Volume Transportado no trecho Uruguaiana-Cacequi
        for i in range(30):
            data_reg = hoje - timedelta(days=i)
            # Oscilação aleatória entre 1000 e 5000 toneladas
            valor_volume = random.uniform(1000, 5000) 
            RegistroDado.objects.create(
                indicador=ind_volume,
                trecho=trechos[0], # Uruguaiana - Cacequi
                valor=round(valor_volume, 2),
                data_registro=data_reg
            )
            
            # Oscilação proporcional para CO2 evitado
            valor_co2 = valor_volume * 0.045
            RegistroDado.objects.create(
                indicador=ind_emissao,
                trecho=trechos[0],
                valor=round(valor_co2, 2),
                data_registro=data_reg
            )
            registros_criados += 2

        self.stdout.write(self.style.SUCCESS(f'{registros_criados} registros históricos gerados para o Dashboard!'))
        self.stdout.write(self.style.SUCCESS('Tudo pronto! Você já pode acessar o Dashboard e ver o mapa e os gráficos.'))
