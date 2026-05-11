FROM python:3.13-alpine

WORKDIR /app

COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY api/ .

RUN adduser -D -u 1001 apiuser && chown -R apiuser:apiuser /app
USER apiuser

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
