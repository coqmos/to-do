FROM python:3.12

RUN pip install --no-cache-dir poetry
COPY . ./app

WORKDIR /app

RUN poetry install --no-dev --no-interaction --no-root

CMD ["poetry", "run", "python", "main.py"]
