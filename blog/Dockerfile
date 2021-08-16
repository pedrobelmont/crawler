FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
RUN apk update &&\
    apk add --no-cache --virtual build-dependencies \
        build-base \
        gcc \
        wget \
        git \
        zlib \
        bash \
        python3-dev \
        jpeg-dev \
        zlib-dev \
        postgresql-dev \
        libxslt-dev \
        linux-headers \
        libxml2-dev \
        libc-dev \
        pcre-dev \
        openssh
ENV LIBRARY_PATH=/lib:/usr/lib
ENV LD_LIBRARY_PATH=/lib:/usr/lib
RUN mkdir -p /requirements/whl/
RUN pip install --upgrade pip

WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt


WORKDIR /app/mysite
COPY ./mysite/mysite /app/mysite
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
