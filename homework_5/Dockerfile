FROM agrigorev/zoomcamp-model:2025

WORKDIR /code

COPY pyproject.toml uv.lock ./

RUN pip install uv
RUN uv sync --frozen

COPY fastapi_docker_service.py .
EXPOSE 8000

CMD ["uv", "run", "uvicorn", "fastapi_docker_service:app", "--host", "0.0.0.0", "--port", "8000"]