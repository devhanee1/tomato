FROM python:3.11

RUN git clone https://github.com/devhanee1/tomato.git

WORKDIR ./tomato
CMD ["python", "./app.py"]

