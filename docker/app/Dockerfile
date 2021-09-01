FROM node:14.15.1 as build-stage
WORKDIR /frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend ./
RUN npm run build

FROM python:3.8.10 as prod-stage
COPY app /opt/app
WORKDIR /opt/app
COPY --from=build-stage /frontend/dist /opt/app/assets
COPY --from=build-stage /frontend/base.html /opt/app/templates
RUN pip3 install --upgrade pip && \
    pip install pipenv
RUN pipenv install --system --deploy