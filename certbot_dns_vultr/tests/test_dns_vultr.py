"""Tests for certbot_dns_vultr.dns_vultr."""

import unittest

import mock
from requests.exceptions import HTTPError

from certbot.compat import os
from certbot.plugins import dns_test_common
from certbot.plugins import dns_test_common_lexicon
from certbot.tests import util as test_util

from certbot_dns_vultr.dns_vultr import Authenticator

TOKEN = 'foo'


class AuthenticatorTest(test_util.TempDirTestCase,
                        dns_test_common_lexicon.BaseLexiconAuthenticatorTest):

    def setUp(self):
        super(AuthenticatorTest, self).setUp()

        path = os.path.join(self.tempdir, 'file.ini')
        dns_test_common.write({"vultr_token": TOKEN}, path)

        self.config = mock.MagicMock(vultr_credentials=path,
                                     vultr_propagation_seconds=0)  # don't wait during tests

        self.auth = Authenticator(self.config, "vultr")

        self.mock_client = mock.MagicMock()
        # _get_vultr_client | pylint: disable=protected-access
        self.auth._get_vultr_client = mock.MagicMock(return_value=self.mock_client)


class VultrLexiconClientTest(unittest.TestCase, dns_test_common_lexicon.BaseLexiconClientTest):

    LOGIN_ERROR = HTTPError('401 Client Error: Unauthorized for url: ...')

    def setUp(self):
        from certbot_dns_vultr.dns_vultr import _VultrLexiconClient

        self.client = _VultrLexiconClient(TOKEN, 0)

        self.provider_mock = mock.MagicMock()
        self.client.provider = self.provider_mock


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
