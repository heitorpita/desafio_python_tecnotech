# Usa uma imagem leve do Python 3.11
FROM python:3.11-slim

# Evita que o Python grave arquivos .pyc no disco
ENV PYTHONDONTWRITEBYTECODE=1
# Evita que o Python bufferize a saída (mostra logs imediatamente)
ENV PYTHONUNBUFFERED=1

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Instala dependências do sistema necessárias para compilar pacotes Python
# (libpq-dev é vital para o driver do Postgres)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de dependências
COPY requirements.txt /app/

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código do projeto para dentro do container
COPY . /app/

# Expõe a porta 8000
EXPOSE 8000

# Comando padrão 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
