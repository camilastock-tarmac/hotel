FROM python:3.12-slim
LABEL maintainer="tarmac.io"

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /scripts
COPY install-system-deps.sh /scripts/install-system-deps.sh
RUN bash /scripts/install-system-deps.sh && rm /scripts/install-system-deps.sh

COPY ./app /app
COPY ./requirements.txt /tmp/requirements.txt

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

ENV PATH="/py/bin:$PATH"

WORKDIR /app
EXPOSE 8000

USER django-user
