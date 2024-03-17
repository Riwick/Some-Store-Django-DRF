FROM python:3.12-alpine

RUN mkdir "Some_Store"

COPY Some_Store /Some_Store

COPY req.txt /Some_Store

WORKDIR /Some_Store

EXPOSE 8000

RUN pip install -r /Some_Store/req.txt