# Use latest Ubuntu docker image
FROM ubuntu:16.04

MAINTAINER Rem Lampa "rem@lansangan.com"

# Update Ubuntu
RUN apt-get -y update

# Install Python 3
RUN apt-get install -y python3 python3-pip

# Migrate configuration files
COPY config /config

# Install Python dependencies
RUN pip3 install -r /config/requirements.txt

# Create server logs folder
RUN mkdir -p /var/log/uwsgi
RUN chown -R root /var/log/uwsgi

# EXPOSE PORT
EXPOSE 80

# Run Flask app via uWSGI
CMD ["/usr/local/bin/uwsgi", "/config/wsgi.docker.ini"]
