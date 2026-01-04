FROM python:3.12.1-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY requirements.txt . 

RUN uv pip install --system -r requirements.txt 

COPY app.py clothing-model.onnx ./

EXPOSE 8080

ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]


