import unittest

from BigHomework import create_app, db


class RunTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def test_run(self, result=None):
        print("OK")



