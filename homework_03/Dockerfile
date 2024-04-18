FROM python:3.9-buster

WORKDIR /var/app
COPY app .

RUN pip install poetry==1.8.2
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD uvicorn app:app --host=0.0.0.0

EXPOSE 8000
