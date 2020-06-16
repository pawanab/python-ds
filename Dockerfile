FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirement.txt /code/
RUN pip3 install -r requirement.txt

COPY . /code/