import unittest
from hello import db, User


class test(unittest.TestCase):
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_name(self):
        user = User("yangbo")
        db.session.add(user)
        db.session.commit()

        result = db.session.query(User).all()[0]
        self.assertEqual(user.username, result.username)

    def test_age(self):
        user = User("yangbo")
        db.session.add(user)
        db.session.commit()

        result = db.session.query(User).all()[0]
        self.assertEqual(user.age, result.age)

    def test_new(self):
        user = User("yangbo", age = 24)
        db.session.add(user)
        db.session.commit()

        result = db.session.query(Use r).all()[0]
        self.assertEqual(user.age, result.age)

if __name__ == '__main__':
    unittest.main()
