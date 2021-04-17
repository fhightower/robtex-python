FROM python:3.9.1-buster

ENV PIP_NO_CACHE_DIR "true"

COPY ./requirements*.txt /code/

WORKDIR /code

RUN pip install bump2version
