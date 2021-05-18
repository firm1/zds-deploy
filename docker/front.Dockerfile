FROM node:10-slim

COPY --from=zds_base:latest /zds /zds

ENV NODE_ENV=development

WORKDIR /zds

RUN apt-get update
RUN apt-get install -y dh-autoreconf

RUN yarn install

RUN yarn run build
