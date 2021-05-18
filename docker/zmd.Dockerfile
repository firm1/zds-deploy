FROM node:10-slim

COPY --from=zds_base:latest /zds /zds

WORKDIR /zds/zmd

RUN npm -g install pm2

RUN npm install --production

