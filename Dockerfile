FROM ubuntu:22.04

RUN apt update && apt install python3 python3-pip -y && pip3 install mysql.connector

RUN mkdir -p /workdir
COPY src /workdir

WORKDIR /workdir

ENTRYPOINT [ "python3", "main.py" ]