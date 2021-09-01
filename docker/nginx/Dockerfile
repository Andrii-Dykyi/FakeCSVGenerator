FROM nginx:alpine

RUN apk add certbot-nginx certbot nano

RUN rm /etc/nginx/conf.d/default.conf

COPY ./docker/nginx/default.conf /etc/nginx/conf.d/