FROM python:3.10-slim

USER 0

RUN mkdir -p /app

COPY src/ app/src
COPY build/docker/entrypoint.sh /app/streamlit_entrypoint.sh
COPY poetry.lock pyproject.toml /app/

RUN apt-get update && \
    python3 -m pip install -U pip && \
    python3 -m pip install poetry && \
    chmod 755 /app/streamlit_entrypoint.sh

WORKDIR /app

EXPOSE 8501

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

ENTRYPOINT ["/app/streamlit_entrypoint.sh"]
