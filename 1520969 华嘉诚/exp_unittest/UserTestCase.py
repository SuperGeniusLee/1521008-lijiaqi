#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# Created by GeniusV on 5/30/18.
import unittest
from hello import db, User


class UserTestCase(unittest.TestCase):
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_1(self):
        user = User("Huajiacheng")
        db.session.add(user)
        db.session.commit()

        result = db.session.query(User).all()[0]
        self.assertEqual(user.username, result.username)

    def test_2(self):
        user = User("Huajiacheng")
        db.session.add(user)
        db.session.commit()

        result = db.session.query(User).all()[0]
        self.assertEqual(user.age, result.age)

    def test_3(self):
        user = User("Huajiacheng", age = 24)
        db.session.add(user)
        db.session.commit()

        result = db.session.query(User).all()[0]
        self.assertEqual(user.age, result.age)

if __name__ == '__main__':
    unittest.main()
