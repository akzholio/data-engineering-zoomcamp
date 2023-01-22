FROM python:3.11-bullseye as base

RUN pip install pandas prefect

WORKDIR /app
COPY pipeline.py pipeline.py

ENTRYPOINT [ "bash" ]
