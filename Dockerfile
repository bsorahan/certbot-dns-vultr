FROM certbot/certbot

RUN mkdir -p /certbot-dns-vultr
COPY setup.py /certbot-dns-vultr
COPY certbot_dns_vultr /certbot-dns-vultr/certbot_dns_vultr

WORKDIR /certbot-dns-vultr
RUN pip install .
