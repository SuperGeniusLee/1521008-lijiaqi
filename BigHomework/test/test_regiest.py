import unittest

from web import create_app, db
from web.models import Post, User


class RunTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test(self):
        user = User()
        user.username = "lijiaqi"
        password = "12345"
        user.password = password
        db.session.add(user)
        db.session.commit()
        result = db.session.query(User).all()[0]
        self.assertTrue(result.verify_password(password))

if __name__ == '__main__':
    unittest.main()
