FROM python:3.8.5

WORKDIR /app

# Install basic development utilities
RUN apt-get update && \
    apt-get install -y python3-dev default-libmysqlclient-dev build-essential && \
    apt-get install -y netcat-openbsd && \
    apt-get install -y bash

# Copy the app folder
COPY ./app /app
# Copy the requirements into app
COPY ./app/requirements.txt /app/requirements.txt
# Copy .env into app
COPY ./.env /app/.env
# Copy docker entrypoint
COPY ./docker/entrypoint.sh /

# Install all packages
RUN pip install -r requirements.txt

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
