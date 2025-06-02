#!/bin/bash
set -e

apt-get update

apt-get install -y --no-install-recommends \
    build-essential \
    libcairo2 \
    pango1.0-tools \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    libjpeg-dev \
    libpng-dev \
    libxml2 \
    libxslt1.1 \
    curl \
    fonts-liberation \
    fonts-dejavu-core \
    python3-dev

apt-get clean
rm -rf /var/lib/apt/lists/*
