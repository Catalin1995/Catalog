import os
import catalog
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, catalog.app.config['DATABASE'] = tempfile.mkstemp()
        catalog.app.config['TESTING'] = True
        self.app = catalog.app.test_client()
        catalog.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(catalog.app.config['DATABASE'])

    def test_empty_db(self):
        return True
        #rv = self.app.get('/')
        #assert 'No entries here so far' in rv.data

if __name__ == '__main__':
    unittest.main()
