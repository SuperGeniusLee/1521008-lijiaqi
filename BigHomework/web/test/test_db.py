import unittest

from web import create_app, db
from web.models import Post, User


class RunTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def test_run(self, result=None):
        print("OK")


    def test_query_all(self):
        a = Post.query.order_by(Post.timestamp.desc()).paginate(
        0, per_page=10,
        error_out=False)
        # print(a)
        # post = Post()
        # post.body = "123"
        # post.author_id = 1
        # post.body_html = "dsdfds"
        # db.session.add(post)
        # db.session.commit()

        # a = db.session.query(Post).all()

        print(a)
        print(a.items)



