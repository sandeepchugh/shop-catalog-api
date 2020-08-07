FROM python:slim

MAINTAINER Sandeep Chugh

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
# COPY requirements and run pip install before
# copying the source code to leverge docker cache
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy project code
COPY ./src /app/

CMD ["python", "/app/app.py"]

