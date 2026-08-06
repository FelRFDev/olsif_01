# OLSIF-CALC / Dashboard

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Django 5.1](https://img.shields.io/badge/Django-5.1-092E20?logo=django)](https://www.djangoproject.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)

![OLSIF-CALC Dashboard Screenshot](https://github.com/user-attachments/assets/4683400d-98e5-4d56-8301-f7eed003c025)

[English Version (README_en.md)](README_en.md)

## 📌 Sobre o Projeto

O **OLSIF-CALC** é a frente tecnológica do **Observatório de Logística Sustentável e Inovação Ferroviária (OLSIF/UNIPAMPA)**. 

A iniciativa busca estudar e produzir inteligência aplicada sobre logística ferroviária, integração regional, dados, inovação tecnológica e desenvolvimento territorial, com atenção especial ao eixo Brasil–Argentina e ao Corredor Mercosul. O foco inicial do observatório é a região de **Uruguaiana–Paso de los Libres** (um dos maiores portos secos da América Latina e gargalo logístico histórico).

### Contexto e Problemática
Historicamente, os dados sobre a malha logística do Mercosul — especialmente no gargalo rodoviário e ferroviário de Uruguaiana-RS — encontram-se fragmentados, subutilizados ou de difícil acesso para tomada de decisão. O transporte intermodal sofre pela falta de visibilidade sobre gargalos e capacidades dos terminais e pátios.

O **OLSIF-CALC** (este projeto) surge exatamente para prover uma **solução tecnológica centralizada**: um repositório estruturado e um painel visual (Dashboard) que unifica informações públicas e acadêmicas de ferrovias, cargas, terminais e fronteiras. Ele transforma dados brutos e dispersos em inteligência acionável, permitindo que pesquisadores e gestores comparem cenários de transporte (custos, emissões de CO2, tempo) e visualizem a malha Sul de forma integrada.

### Princípios da Elaboração
A ideia central desta aplicação é **transformar infraestrutura física em redes inteligentes, sustentáveis e orientadas por dados**. 
Para viabilizar isso, o MVP foi projetado com três princípios arquitetônicos:
1. **Simplicidade de Colaboração:** Utiliza Python/Django puro, permitindo que estudantes e pesquisadores (com pouco conhecimento avançado de frontend) consigam contribuir rapidamente sem barreiras de frameworks Javascript complexos.
2. **Escalabilidade (API-First):** O sistema não é apenas um site, é um servidor de dados (APIs RESTful em JSON) desenhado para ser consumido no futuro por aplicativos mobile, simulações matemáticas e inteligência artificial.
3. **Foco Geográfico:** A plataforma utiliza o Leaflet.js para focar geograficamente a infraestrutura na fronteira.

---

## 🏗️ Arquitetura e Tecnologias

* **Backend & API:** Python 3.11 + Django + Django REST Framework.
* **Banco de Dados:** PostgreSQL (preparado para PostGIS futuramente) ou SQLite3 em ambiente local não-dockerizado.
* **Frontend Dashboard:** Renderização via Templates do Django, com estilização em **Tailwind CSS** (via CDN para simplicidade) e bibliotecas JavaScript modernas (**Chart.js** para gráficos e **Leaflet.js** para mapas espaciais).
* **Infraestrutura/DevOps:** Docker & Docker Compose para garantia de padronização de ambientes (Windows, Mac, Linux).

---

## 🗺️ Interfaces e Rotas Disponíveis

O sistema provê interfaces tanto para leitura humana quanto para consumo de máquinas (sistemas de IA/Analytics).

### Interfaces Web (Para Usuários)
* `http://localhost:8000/` -> **Dashboard Interativo:** Painel visual contendo o mapa da malha logística, os cartões de indicadores (KPIs) e o gráfico dinâmico comparativo.
* `http://localhost:8000/admin/` -> **Painel de Gestão (Django Admin):** Interface restrita e segura para que os pesquisadores insiram e editem os dados de terminais, cargas, e trechos ferroviários, sem a necessidade de conhecimento em banco de dados.

### APIs REST (Para Integração e Cientistas de Dados)
A rota base da API pode ser explorada interativamente pelo navegador em `http://localhost:8000/api/`. Todas as APIs aceitam os métodos padrão REST (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`):

* `/api/terminais/` - Retorna a lista de Terminais Logísticos (Porto Seco, Pátios, Áreas de Transbordo) com coordenadas geoespaciais.
* `/api/trechos/` - Rotas ferroviárias mapeadas contendo distâncias e status operacional.
* `/api/indicadores/` - O "dicionário" de métricas estudadas (ex: Emissões CO2 Evitadas, Volume).
* `/api/registros/` - As Séries Históricas, vinculando um Terminal/Trecho a um Indicador num determinado tempo.

---

## 🚀 Como Rodar e Testar o Projeto Localmente

Existem duas formas principais de rodar o ambiente na sua máquina local: **Usando Docker** (Recomendado para simular o ambiente de produção completo com PostgreSQL) ou **Usando Python puro** (Ideal para estudantes que preferem o SQLite).

### Opção 1: Via Python Local (Ambiente Leve)
Se você possui Python instalado na máquina:

1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Crie a base de dados (SQLite automático):**
   ```bash
   python backend/manage.py makemigrations logistica
   python backend/manage.py migrate
   ```
3. *(Opcional)* **Gere dados de demonstração no banco:**
   ```bash
   python backend/manage.py seed_data
   ```
4. **Crie um superusuário para o Admin:**
   ```bash
   python backend/manage.py createsuperuser
   ```
5. **Inicie o servidor de testes:**
   ```bash
   python backend/manage.py runserver
   ```
6. Abra `http://localhost:8000` em seu navegador.

### Opção 2: Via Docker Compose (Recomendado)
Certifique-se de que o Docker e Docker Compose estão instalados e ativos.

1. **Suba a estrutura completa (Banco PostgreSQL + Servidor Web Django):**
   ```bash
   docker-compose up -d --build
   ```
2. **Execute as migrações no contêiner web:**
   ```bash
   docker-compose exec web python backend/manage.py makemigrations logistica
   docker-compose exec web python backend/manage.py migrate
   ```
3. *(Opcional)* **Gere os dados fictícios:**
   ```bash
   docker-compose exec web python backend/manage.py seed_data
   ```
4. **Crie o superusuário:**
   ```bash
   docker-compose exec web python backend/manage.py createsuperuser
   ```

---

## 🤝 Como Contribuir
O OLSIF é uma iniciativa aberta. Se você é estudante da UNIPAMPA ou pesquisador entusiasta de logística e sustentabilidade:

1. Dê um Fork no projeto.
2. Veja as _Issues_ no repositório marcadas como `good first issue`.
3. Desenvolva suas simulações matemáticas (podemos integrar bibliotecas como `pandas` ou `scipy` em rotas da API).
4. Submeta seu _Pull Request_.

*Desenvolvido como projeto estratégico para integrar o Corredor Mercosul.*
