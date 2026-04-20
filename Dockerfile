# Imagem base oficial do Python
FROM python:3.12-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia todos os arquivos do projeto
COPY . .

# Instala o pylint (usado no CI) e o pytest
RUN pip install --no-cache-dir pylint pytest

# Comando padrão: roda os testes ao iniciar o container
CMD ["python", "-m", "pytest", "test_imc.py", "-v"]