FROM alpine

ARG GIT_USER
ARG GIT_BRANCH

WORKDIR /zds

RUN wget -q https://github.com/${GIT_USER}/zds-site/archive/${GIT_BRANCH}.tar.gz -O deploy.tar.gz
RUN tar -xf deploy.tar.gz
RUN cp -rp zds-site-`echo ${GIT_BRANCH} | sed -r 's/\//-/g' | sed -r 's/^v//g'`/* .
RUN rm -rf deploy.tar.gz
RUN rm -rf zds-site-`echo ${GIT_BRANCH} | sed -r 's/\//-/g' | sed -r 's/^v//g'`

COPY ./settings_docker.py /zds/zds/settings/docker.py
COPY ./service/zds-index.sh /zds/zds-index.sh


