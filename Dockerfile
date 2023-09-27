FROM python:3.9-slim

WORKDIR /app

RUN apt-get -qq update && apt-get -qq install curl libpq-dev gcc 1> /dev/null

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
