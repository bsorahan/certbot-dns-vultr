# Certbot-dns-vultr
Certbot-dns-vultr is an authenticator plugin for [Certbot](https://certbot.eff.org/) to configure [Vultr](https://www.vultr.com/) to respond to ACME dns-01 challenges to obtain HTTPS certificates. Certbot is the tool which is commonly used to automatically obtain, renew and install certificates issued by [Let's Encrypt](https://letsencrypt.org/) or any other CA that uses the ACME protocol.

The plugin uses the Vultr API along with your API Key to temporarily configure DNS records so that a CA can verify that you own a domain and issue a HTTPS certificate.

## Setup certbot-dns-vultr
The certbot-dns-vultr plugin can be installed using pip.
```sh
pip install .
```
Python [pip](https://pypi.org/project/pip/) and [setuptools](https://pypi.org/project/setuptools/) will need to be installed on your system.

For Ubuntu 18.04 these can be installed by:
```sh
apt-get update
apt-get -y install python-pip python-setuptools python-wheel
```

## Usage
To obtain a HTTPS certificates for a list of domains run:
```sh
VULTR_API_KEY="YOUR KEY"
CREDENTIALS_FILE=$HOME/vultr_credentials.ini
DOMAINS=example.com,abc.example.com,www.example.com,*.dev.example.com
EMAIL=ben@example.com
echo "dns_vultr_token = $VULTR_API_KEY" > $CREDENTIALS_FILE
chmod 600 $CREDENTIALS_FILE
certbot certonly --domains $DOMAINS --email $EMAIL \
  --authenticator dns-vultr \
  --dns-vultr-credentials $CREDENTIALS_FILE
```
Set `VULTR_API_KEY`, `CREDENTIALS_FILE`, `DOMAINS` and `EMAIL` as required for your environment.

Your `VULTR_API_KEY` can be retrieved from your Vultr account: https://my.vultr.com/settings/#settingsapi.

## Docker
Alternatively, can be run in docker as follows.

Build the docker image
``` sh
docker build -t local/certbot-dns-vultr .
```

Run certbot in docker to generate certificates using the certbot-dns-vultr authenticator
``` sh
VULTR_API_KEY="YOUR KEY"
CREDENTIALS_FILE=$HOME/vultr_credentials.ini
DOMAINS=example.com,abc.example.com,www.example.com,*.dev.example.com
EMAIL=ben@example.com
CERTS_DIR=$HOME/certs
echo "dns_vultr_token = $VULTR_API_KEY" > $CREDENTIALS_FILE
mkdir -p $CERTS_DIR
docker run -it -v $CREDENTIALS_FILE:/credentials.ini -v $CERTS_DIR:/etc/letsencrypt/live local/certbot-dns-vultr certonly --authenticator dns-vultr --dns-vultr-credentials /credentials.ini --domains "$DOMAINS" -m $EMAIL -v
```
### Advanced Usage 
Refer to certbot documentation for usage of certbot https://certbot.eff.org/docs/using.html. As certbot-dns-vultr is a plugin for certbot the documentation describes other common usage such as combining with other plugins to automate certificate installation and renewal.

For certbot-dns-vultr plugin configuration options run:
```sh
certbot --help certbot-dns-vultr:dns-vultr
```
