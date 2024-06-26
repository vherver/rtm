FROM python:3.9

WORKDIR /app
COPY /requirements/base.txt /app/requirements/base.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements/base.txt
COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]