import unittest
from hello530 import db
from hello530 import User

class testUser(unittest.TestCase):
	def	setUp(self):
		db.create_all()
	def tearDown(self):
		db.drop_all()
	def	test_1(self):
		user=User('baochangping')
		db.session.add(user)
		db.session.commit()
		result=db.session.query(User).all()[0]
		self.assertEqual(user.username,result.username)
		
	def	test_2(self):
		user=User('baochangping')
		db.session.add(user)
		db.session.commit()
		result=db.session.query(User).all()[0]
		self.assertEqual(user.age,result.age)
	def	test_3(self):
		user=User('baochangping',age=24)
		db.session.add(user)
		db.session.commit()
		result=db.session.query(User).all()[0]
		self.assertEqual(user.age,result.age)
if __name__ == '__main__':
		unittest.main()
