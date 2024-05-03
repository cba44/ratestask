FROM python:3.12.3-alpine
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ratestask.py ratestask.py
COPY app app

EXPOSE 80

CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]