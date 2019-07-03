#!/bin/sh

echo "certbot_dns_vultr:dns_vultr_token = $API_KEY" > /opt/certbot/credentials.ini
chmod 600 /opt/certbot/credentials.ini

certbot certonly -n \
$CERTBOT_ARGS \
-a certbot-dns-vultr:dns-vultr  \
--certbot-dns-vultr:dns-vultr-credentials /opt/certbot/credentials.ini \
--agree-tos --manual-public-ip-logging-ok \
-d "$DOMAIN" -m $EMAIL
