FROM python:3.12.0

WORKDIR /app

COPY ./src /app/src
COPY ./requirements.txt /app/requirements.txt
COPY ./tests /app/tests

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]