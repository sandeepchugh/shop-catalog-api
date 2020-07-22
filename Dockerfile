FROM python:slim

# COPY requirements and run pip install before
# copying the source code to leverge docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./src /app

CMD ["python", "app.py"]

