import unittest

from web import create_app, db
from web.models import Post, User


class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
	
    def test_post(self):
        a=Post.query.order_by(Post.timestamp.desc()).paginate(0,per_page=10,error_out=False)
        print(a.items[0])

if __name__ == '__main__':
    unittest.main()
