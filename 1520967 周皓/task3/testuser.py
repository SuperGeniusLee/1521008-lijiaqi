import unittest
from hello import User
from hello import db

class TestUser(unittest.TestCase):
    
    def setUp(self):
        db.create_all()
    def tearDown(self):
    	db.drop_all()
    def test_user(self):
        user=User("zhouhao")
        db.session.add(user)
        db.session.commit()
        result = db.session.query(User).all()[0]
        self.assertEqual(user.username,result.username)
    def test_age(self):
        user=User("zhouhao")
        db.session.add(user)
        db.session.commit()
        result = db.session.query(User).all()[0]
        self.assertEqual(user.age,result.age)
    def test_reset(self):
        user=User("zhouhao",age=21)
        db.session.add(user)
        db.session.commit()
        result = db.session.query(User).all()[0]
        self.assertEqual(user.age,result.age)
        
	
if __name__ == '__main__':
    unittest.main()
