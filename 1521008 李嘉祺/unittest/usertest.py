import unittest
from hello import db,User


class UserTest(unittest.TestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test(self):
        user = User("lijiaqi")
        db.session.add(user)
        db.session.commit()
        result = db.session.query(User).all()[0]
        self.assertEqual(user.username, result.username)


    def test1(self):
        user = User("lijiaqi")
        db.session.add(user)
        db.session.commit()

        result = db.session.query(User).all()[0]
        self.assertEqual(user.age, result.age)


    def test2(self):
        user = User("lijiaqi", age=24)
        db.session.add(user)
        db.session.commit()

        result = db.session.query(User).all()[0]
        self.assertEqual(user.age, result.age)
        
if __name__ == '__main__':
    unittest.main()
