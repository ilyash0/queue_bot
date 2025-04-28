FROM ghcr.io/astral-sh/uv:0.5-python3.12-alpine

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

COPY . .

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen \
    && adduser -D appuser \
    && chown -R appuser:appuser .

USER appuser

CMD ["python", "/app/source/__main__.py"]

EXPOSE 8080