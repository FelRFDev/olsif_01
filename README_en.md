# OLSIF-CALC / Dashboard

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Django 5.1](https://img.shields.io/badge/Django-5.1-092E20?logo=django)](https://www.djangoproject.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)

[Versão em Português (README.md)](README.md)

## 📌 About the Project

**OLSIF-CALC** is the technological front of the **Observatory of Sustainable Logistics and Railway Innovation (OLSIF/UNIPAMPA)**.

This initiative aims to study and produce applied intelligence on railway logistics, regional integration, data, technological innovation, and territorial development, focusing specifically on the Brazil–Argentina axis and the Mercosur Corridor. The initial territorial focus is the **Uruguaiana–Paso de los Libres** region (one of Latin America's largest dry ports and a historical logistical bottleneck).

### Context and Problem Statement
Historically, data regarding the Mercosur logistics network — especially in the Uruguaiana-RS road and railway bottleneck — has been fragmented, underutilized, or difficult to access for decision-making. Intermodal transport suffers from a lack of visibility regarding bottlenecks and the capacities of terminals and yards.

**OLSIF-CALC** (this project) was created precisely to provide a **centralized technological solution**: a structured repository and a visual dashboard that unifies public and academic information about railways, cargo, terminals, and borders. It transforms raw, scattered data into actionable intelligence, allowing researchers and managers to compare transport scenarios (costs, CO2 emissions, time) and visualize the southern network in an integrated manner.

### Design Principles
The core idea of this application is to **transform physical infrastructure into smart, sustainable, and data-driven networks**. 
To make this viable, the MVP was designed with three architectural principles:
1. **Collaboration Simplicity:** Built with pure Python/Django, allowing students and researchers (even those with little advanced frontend knowledge) to contribute quickly without the barriers of complex JavaScript frameworks.
2. **Scalability (API-First):** The system isn't just a website; it's a data server (RESTful APIs serving JSON), designed to be consumed in the future by mobile apps, mathematical simulations, and artificial intelligence.
3. **Geographic Focus:** The platform leverages Leaflet.js to geographically focus on the border infrastructure.

---

## 🏗️ Architecture and Technologies

* **Backend & API:** Python 3.11 + Django + Django REST Framework.
* **Database:** PostgreSQL (prepared for PostGIS in the future) or SQLite3 in local non-dockerized environments.
* **Frontend Dashboard:** Rendered via Django Templates, styled with **Tailwind CSS** (via CDN for simplicity), and integrated with modern JavaScript libraries (**Chart.js** for charts and **Leaflet.js** for spatial maps).
* **Infrastructure/DevOps:** Docker & Docker Compose to ensure environment standardization across OS (Windows, Mac, Linux).

---

## 🗺️ Interfaces and Available Routes

The system provides interfaces for both human reading and machine consumption (AI/Analytics systems).

### Web Interfaces (For Users)
* `http://localhost:8000/` -> **Interactive Dashboard:** Visual panel containing the logistics network map, key performance indicators (KPIs) cards, and a dynamic comparative chart.
* `http://localhost:8000/admin/` -> **Management Panel (Django Admin):** A restricted, secure interface for researchers to insert and edit data regarding terminals, cargo, and railway sections without needing any database expertise.

### REST APIs (For Integration and Data Scientists)
The base API route can be interactively explored via browser at `http://localhost:8000/api/`. All APIs accept standard REST methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`):

* `/api/terminais/` - Returns the list of Logistics Terminals (Dry Ports, Yards, Transshipment Areas) with geospatial coordinates.
* `/api/trechos/` - Mapped railway routes containing distances and operational statuses.
* `/api/indicadores/` - The "dictionary" of studied metrics (e.g., Avoided CO2 Emissions, Volume).
* `/api/registros/` - Time Series records, linking a Terminal/Route to an Indicator at a specific time.

---

## 🚀 How to Run and Test Locally

There are two primary ways to run the environment on your local machine: **Using Docker** (Recommended for simulating the full production environment with PostgreSQL) or **Using pure Python** (Ideal for students who prefer SQLite).

### Option 1: Via Local Python (Lightweight Environment)
If you have Python installed on your machine:

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Create the database (automatic SQLite):**
   ```bash
   python backend/manage.py makemigrations logistica
   python backend/manage.py migrate
   ```
3. *(Optional)* **Generate demonstration data in the database:**
   ```bash
   python backend/manage.py seed_data
   ```
4. **Create a superuser for the Admin panel:**
   ```bash
   python backend/manage.py createsuperuser
   ```
5. **Start the development server:**
   ```bash
   python backend/manage.py runserver
   ```
6. Open `http://localhost:8000` in your web browser.

### Option 2: Via Docker Compose (Recommended)
Make sure Docker and Docker Compose are installed and running.

1. **Bring up the full infrastructure (PostgreSQL DB + Django Web Server):**
   ```bash
   docker-compose up -d --build
   ```
2. **Execute migrations in the web container:**
   ```bash
   docker-compose exec web python backend/manage.py makemigrations logistica
   docker-compose exec web python backend/manage.py migrate
   ```
3. *(Optional)* **Generate mock data:**
   ```bash
   docker-compose exec web python backend/manage.py seed_data
   ```
4. **Create the superuser:**
   ```bash
   docker-compose exec web python backend/manage.py createsuperuser
   ```

---

## 🤝 How to Contribute
OLSIF is an open initiative. If you are a UNIPAMPA student or an enthusiastic researcher in logistics and sustainability:

1. Fork the project.
2. Check out the _Issues_ in the repository marked as `good first issue`.
3. Develop your mathematical simulations (we can integrate libraries like `pandas` or `scipy` into API routes).
4. Submit your _Pull Request_.

*Developed as a strategic project to integrate the Mercosur Corridor.*
