FROM python:3.12-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_NO_DEV=1

COPY . /app

WORKDIR /app

RUN uv sync --locked

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

CMD [ "uv", "run", "main.py"]
