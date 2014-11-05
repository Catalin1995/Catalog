import catalog
import os
import unittest

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        catalog.app.config['TESTING'] = True
        self.app = catalog.app.test_client()


class catalogTestCase(unittest.TestCase):
    def test_sum(self):
        assert 1+1 == 2

if (__name__ == '__main__'):
    unittest.main()
