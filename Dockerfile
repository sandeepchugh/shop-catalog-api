FROM python:slim

MAINTAINER Sandeep Chugh

# COPY requirements and run pip install before
# copying the source code to leverge docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements.txt

# Copy project code
COPY ./src /app

CMD ["python", "app.py"]

