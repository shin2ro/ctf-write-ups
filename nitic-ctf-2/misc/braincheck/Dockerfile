FROM ubuntu:focal
RUN apt update \
    && apt install -y bf \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*
