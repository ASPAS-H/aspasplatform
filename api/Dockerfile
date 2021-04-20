FROM python:3.9
WORKDIR /usr/aspas/api

COPY . /usr/aspas/api

RUN pip install flask
EXPOSE 5000
CMD python src/app.py