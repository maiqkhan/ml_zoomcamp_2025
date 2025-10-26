FROM python:3.12.3-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

COPY .python-version pyproject.toml uv.lock ./

RUN uv sync --locked


COPY ./5-deployment/predict.py ./5-deployment/model.bin ./

EXPOSE 9696 

ENTRYPOINT ["uvicorn", "predict:app", "--host" , "0.0.0.0", "--port", "9696"]
