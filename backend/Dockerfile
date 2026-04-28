ARG PYTHON_BUILD_BASE_IMAGE=python:3.12-bookworm
ARG PYTHON_RUNTIME_BASE_IMAGE=python:3.12-slim-bookworm

FROM ${PYTHON_BUILD_BASE_IMAGE} AS build
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY --from=ghcr.io/astral-sh/uv:0.10.7 /uv /uvx /bin/

COPY pyproject.toml uv.lock README.md ./
RUN ["uv", "sync", "--locked", "--no-dev"]

COPY . .

FROM ${PYTHON_RUNTIME_BASE_IMAGE}
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY --from=ghcr.io/astral-sh/uv:0.10.7 /uv /uvx /bin/
COPY --from=build /app /app
COPY entrypoint.py /entrypoint.py

ENTRYPOINT ["python", "/entrypoint.py"]
EXPOSE 8000
CMD ["uv", "run", "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
