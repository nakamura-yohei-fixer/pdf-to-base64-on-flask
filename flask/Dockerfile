FROM python:3.7
USER root

RUN apt-get update
RUN apt-get install -y poppler-utils poppler-data

ARG project_dir=/app/

WORKDIR $project_dir

RUN pip install flask
RUN pip install pdf2image
RUN pip install pillow
RUN pip install wheel

CMD ["python", "main.py"]
