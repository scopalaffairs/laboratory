FROM python:3.10.3-slim AS base

RUN apt-get update

WORKDIR /app

COPY app/commands/start.sh /

ENV POETRY_VIRTUALENVS_IN_PROJECT="false"
RUN pip install poetry==1.1.7
COPY app/pyproject.toml app/poetry.lock /app/

RUN poetry install

ENTRYPOINT ["bash", "/start.sh"]
