# Backend
FROM alpine:latest

RUN apk add python3-dev \
    && apk add py3-pip \
    && pip3 install --upgrade pip

WORKDIR /APP

COPY . /APP

RUN pip install --user flask
RUN pip install --user flask_cors
RUN pip install --user requests
RUN pip install --user python-dotenv

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["api.py"]