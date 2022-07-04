FROM python:3.8.10
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . /app
CMD ./manage.py runserver 0.0.0.0:8000