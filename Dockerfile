FROM certbot/certbot

COPY src src/certbot-dns-vultr

RUN pip install --no-cache-dir --editable src/certbot-dns-vultr

ENTRYPOINT ./src/certbot-dns-vultr/docker-run.sh 
