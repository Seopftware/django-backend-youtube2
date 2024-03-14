# 도커 이미지 구축
# alpine: Linux 경량화
FROM python:3.11-alpine3.19

LABEL maintainer='seopftware'

# 파이썬 관련 로그를 확인할 수 있게 해주는 옵션 (기본값은 0=False)
ENV PYTHONUNBUFFERED 1

# 로컬에서 작업한 파일들을 가상환경으로 복사하는 코드
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false

# 리눅스 -> venv
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true"]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user 

ENV PATH="/py/bin:$PATH"

USER django-user