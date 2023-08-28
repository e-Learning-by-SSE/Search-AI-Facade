# syntax=docker/dockerfile:1.4
FROM python:3.11.2-slim-buster AS builder

WORKDIR /code

COPY requirements.txt /code
RUN pip install --upgrade pip
RUN pip install python-dotenv
RUN pip3 install -r requirements.txt

COPY . /code

ENTRYPOINT ["python3"]
CMD ["app.py"]

