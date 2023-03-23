# ./django-docker/app/Dockerfile
FROM python:3.8.10
# set work directory
WORKDIR /opt/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
# install dependencies
RUN pip install --upgrade pip
RUN apt update
RUN apt install build-essential pulseaudio portaudio19-dev -y
COPY ./requirements.txt /opt/app/requirements.txt 
RUN chmod +x /opt/app/requirements.txt
RUN pip3 install -r requirements.txt
# copy project
COPY . /opt/app/