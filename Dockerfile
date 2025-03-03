FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /app
COPY ./requirements.txt /tmp/requirements.txt
COPY . /app/
EXPOSE 8000



RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp



CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]