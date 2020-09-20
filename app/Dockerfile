FROM python:3.8.5-buster

WORKDIR /app

ADD . /app

RUN pip install uwsgi

CMD ["uwsgi" , "uwsgi-test.ini"]
