ARG PYTHON_BASE_IMAGE
FROM ${PYTHON_BASE_IMAGE}
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_NO_DEV=1

COPY --from=ghcr.io/astral-sh/uv:0.10.0 /uv /uvx /bin/

COPY . .
RUN uv sync --locked --no-dev
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 8000
CMD ["uv", "run", "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
