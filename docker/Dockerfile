# pull official base image
FROM python:3.9.5

# set work directory
WORKDIR /var/www/SITE_ALAN

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY . requirements.txt /
RUN pip install --upgrade pip
RUN pip3 install -r /requirements.txt

# copy project
COPY . /var/www/SITE_ALAN