import unittest

from web import create_app, db
from web.models import Comment


class TestCase(unittest.TestCase):
       
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    def test_commets(self):
            
        a = Comment.query.order_by(Comment.timestamp.desc()).paginate(0, per_page=10,error_out=False)
        print(a.items[0])
        
if __name__ == '__main__':
    unittest.main()
