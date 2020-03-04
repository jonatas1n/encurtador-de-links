FROM python:3.7

RUN mkdir /code
WORKDIR /code 

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
WORKDIR /code/src