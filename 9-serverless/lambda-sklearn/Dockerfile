FROM public.ecr.aws/lambda/python:3.13
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

COPY requirements.txt ./
RUN uv pip install  --system -r requirements.txt

COPY lambda_function.py model.bin ./

CMD ["lambda_function.lambda_handler"]