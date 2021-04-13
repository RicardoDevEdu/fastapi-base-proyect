FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get install -y gcc python3-dev \
  && apt-get -y install libffi-dev

WORKDIR /www

COPY . /www/

COPY ./requirements/ /www/requirements/

RUN pip3 install -r requirements/local.txt

COPY docker/local/django_start /django_start

RUN chmod +x /django_start
