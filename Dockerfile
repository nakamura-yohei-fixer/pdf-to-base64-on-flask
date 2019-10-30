FROM python:3.7-alpine
USER root

ARG project_dir=/app/

WORKDIR $project_dir

COPY app/main.py /app/

RUN set -x && \
  : "update apk" && \
  apk update && \
  : "update apk packages" && \
  apk --update add libxml2-dev \
  libxslt-dev \
  libffi-dev \
  gcc \
  musl-dev \
  libgcc \openssl-dev \
  curl && \
  : "add apk packages" && \
  apk --no-cache add poppler-utils \ 
  jpeg-dev \
  zlib-dev \
  freetype-dev \
  lcms2-dev \
  openjpeg-dev \
  tiff-dev \
  tk-dev \
  tcl-dev \
  harfbuzz-dev \
  fribidi-dev && \
  : "install pip packages" && \
  pip install --upgrade pip setuptools && \
  pip install flask wheel pdf2image Pillow

EXPOSE 80

CMD ["python", "main.py"]
