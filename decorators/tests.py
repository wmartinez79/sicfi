# Run this test with python test.py directly. Does not require
# Django's "python manage.py test" facility.

import unittest
import addgene.decorators

class _Settings(object):
    pass

class TestCase(unittest.TestCase):
    def test_is_ssl_port_80(self):
        settings = _Settings()
        self.assertFalse(addgene.decorators._is_ssl_port(settings, 80))

    def test_is_ssl_port_443(self):
        settings = _Settings()
        self.assertTrue(addgene.decorators._is_ssl_port(settings, 443))

    def test_is_ssl_port_8443(self):
        settings = _Settings()
        settings.SSL_PORT = 8443
        self.assertTrue(addgene.decorators._is_ssl_port(settings, 8443))

if __name__ == '__main__':
    unittest.main()

