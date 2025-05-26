FROM ubuntu:latest

ENV FLAG_PREFIX="placeholder"
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
 && apt-get install -y debconf-utils \
 && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
 && apt-get install -y slapd ldap-utils \
 && rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    gcc \
    build-essential \
    libsasl2-dev \
    python-dev-is-python3 \
    libldap2-dev \
    libssl-dev \
    gunicorn

COPY app/requirements.txt /app/requirements.txt
RUN python3 -m pip install --break-system-packages -r /app/requirements.txt

COPY debconf_selections.txt /tmp/debconf_selections.txt
RUN cat /tmp/debconf_selections.txt | debconf-set-selections

RUN dpkg-reconfigure -f noninteractive slapd
COPY app /app

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY base.ldif /base.ldif

CMD /entrypoint.sh
