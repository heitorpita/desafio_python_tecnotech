# 🎓 Sistema de Gestão Escolar - Academia Dev Python 2026.1

Sistema completo de gestão de alunos, cursos e matrículas desenvolvido com **Django**, **Django REST Framework**, **PostgreSQL** e **Docker**.

---

## 📋 Funcionalidades Implementadas

### ✅ Cadastros (CRUD Completo)
- **Alunos:** Nome, Email, CPF, Data de Ingresso
- **Cursos:** Nome, Carga Horária, Valor, Status (Ativo/Inativo)
- **Matrículas:** Vincular aluno a curso, registrar status de pagamento

### 📊 Dashboards e Relatórios
- Painel Financeiro (Total pago/devido por aluno)
- Dashboard Geral
- Histórico Detalhado do Aluno

### 🔌 API REST (DRF)
- Endpoints completos para todas as entidades
- Relatórios via JSON (Agregações e SQL Bruto)
- Filtros e operações especiais (Marcar como pago, listar por aluno)

### 🐘 Requisitos SQL
- Arquivo `meu_database.sql` com DDL completo
- Endpoint demonstrando SQL RAW com JOIN, SUM, COUNT, GROUP BY

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| Python | 3.11+ | Linguagem base |
| Django | 5.2+ | Framework web |
| Django REST Framework | 3.14+ | API REST |
| PostgreSQL | 15 | Banco de dados |
| Docker & Docker Compose | 24+ | Containerização |
| Bootstrap | 5.3 | Interface frontend |

---

## 🚀 Como Rodar o Projeto (Docker)

### Pré-requisitos
- Docker instalado ([Download aqui](https://www.docker.com/get-started))
- Docker Compose (geralmente já vem com o Docker Desktop)

### Passo 1: Clone o Repositório

git clone https://github.com/heitorpita/desafio_python_tecnotech.git

cd desafio_python_tecnotech

### Passo 2: Suba os Containers

docker-compose up --build

### Passo 3: Acesse a Aplicação


## 🌐 URLs Principais

### Frontend (HTML)

| Lista de Alunos | http://localhost:8000/alunos/ | 

| Lista de Cursos | http://localhost:8000/cursos/ | 

| Lista de Matrículas | http://localhost:8000/matriculas/ | 

| Dashboard Geral | http://localhost:8000/matriculas/dashboard/ |

| Painel Financeiro | http://localhost:8000/matriculas/financeiro/ | 

| Histórico do Aluno (ID 1) | http://localhost:8000/matriculas/relatorio/aluno/1/ | 

### API (JSON)
#### Alunos
- `GET /alunos/api/` - Listar todos
- `POST /alunos/api/` - Criar novo
- `GET /alunos/api/{id}/` - Detalhes
- `PUT /alunos/api/{id}/` - Atualizar
- `DELETE /alunos/api/{id}/` - Remover
- `GET /alunos/api/alunos/{id}/matriculas/` - Matrículas do aluno

#### Cursos
- `GET /cursos/api/` - Listar todos
- `POST /cursos/api/` - Criar novo
- `GET /cursos/api/{id}/` - Detalhes
- `PUT /cursos/api/{id}/` - Atualizar
- `DELETE /cursos/api/{id}/` - Remover
- `GET /cursos/api/stats/` - **Total de matrículas por curso**
- `GET /cursos/api/relatorio-sql/` - **SQL**

#### Matrículas
- `GET /matriculas/api/` - Listar todas
- `POST /matriculas/api/` - Criar matrícula
- `GET /matriculas/api/{id}/` - Detalhes
- `PATCH /matriculas/api/{id}/pagar/` - **Marcar como PAGO**
- `DELETE /matriculas/api/{id}/` - Remover

#### Relatórios Financeiros (API)
- `GET /matriculas/api/financeiro/totais/` - Total pago/devido por aluno
- `GET /matriculas/api/financeiro/global/` - Totais gerais da escola