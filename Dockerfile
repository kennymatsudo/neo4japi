FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./app /app

EXPOSE 80

WORKDIR /app

RUN pip install -r requirements.txt
