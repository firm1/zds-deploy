FROM python:3.9

COPY --from=zds_base:latest /zds /zds

ENV PYTHONUNBUFFERED 1

WORKDIR /zds

ENV DOCKERIZE_VERSION v0.6.1
RUN wget -q https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

COPY ./settings_docker.py /zds/zds/settings/docker.py
COPY ./service/zds-index.sh /zds/zds-index.sh

RUN pip3 -q install -r /zds/requirements-dev.txt
RUN pip3 -q install -r /zds/requirements-prod.txt
