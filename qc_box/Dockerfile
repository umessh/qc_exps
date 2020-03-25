FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3-pip python3-dev

RUN cd /usr/local/bin && ln -s /usr/bin/python3 python && pip3 install --upgrade pip

RUN pip install qiskit

RUN pip install notebook
RUN pip install matplotlib

RUN mkdir -p /var/www/qc_box

WORKDIR /var/www/qc_box

ENV IBMQX_KEY your_key