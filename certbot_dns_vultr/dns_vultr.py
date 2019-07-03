"""DNS Authenticator for Vultr DNS."""
import logging

import zope.interface
from lexicon.providers import vultr

from certbot import errors
from certbot import interfaces
from certbot.plugins import dns_common
from certbot.plugins import dns_common_lexicon

logger = logging.getLogger(__name__)

ACCOUNT_URL = 'https://my.vultr.com/settings/#settingsapi'


@zope.interface.implementer(interfaces.IAuthenticator)
@zope.interface.provider(interfaces.IPluginFactory)
class Authenticator(dns_common.DNSAuthenticator):
    """DNS Authenticator for Vultr

    This Authenticator uses the Vultr v2 API to fulfill a dns-01 challenge.
    """

    description = ('Obtain certificates using a DNS TXT record '
        '(if you are using Vultr for DNS).')
    ttl = 60

    def __init__(self, *args, **kwargs):
        super(Authenticator, self).__init__(*args, **kwargs)
        self.credentials = None

    @classmethod
    def add_parser_arguments(cls, add):  # pylint: disable=arguments-differ
        super(Authenticator, cls).add_parser_arguments(add, 
            default_propagation_seconds=30)
        add('credentials', help='Vultr credentials INI file.')

    def more_info(self):  # pylint: disable=missing-docstring,no-self-use
        return ('This plugin configures a DNS TXT record to respond to '
            'a dns-01 challenge using the Vultr API.')

    def _setup_credentials(self):
        self.credentials = self._configure_credentials(
            'credentials',
            'Vultr credentials INI file',
            {
                'token': 'User access token for Vultr v2 API. '
                '(See {0}.)'.format(ACCOUNT_URL)
            }
        )

    def _perform(self, domain, validation_name, validation):
        self._get_vultr_client().add_txt_record(domain, validation_name, validation)

    def _cleanup(self, domain, validation_name, validation):
        self._get_vultr_client().del_txt_record(domain, validation_name, validation)

    def _get_vultr_client(self):
        return _VultrLexiconClient(self.credentials.conf('token'), self.ttl)


class _VultrLexiconClient(dns_common_lexicon.LexiconClient):
    """
    Encapsulates all communication with the Vultr via Lexicon.
    """

    def __init__(self, token, ttl):
        super(_VultrLexiconClient, self).__init__()

        self.provider = vultr.Provider({
            'auth_token': token,
            'ttl': ttl,
        })

    def _handle_http_error(self, e, domain_name):

        return errors.PluginError(('HTTP error '
            'for {0}: {1}. (Is your API token value correct?)')
            .format(domain_name, e))
