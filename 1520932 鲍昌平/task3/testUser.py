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
		self.assertEqual(user.username,result.username,msg="实际结果不符合预期结果")
		
	def	test_2(self):
		user=User('baochangping')
		db.session.add(user)
		db.session.commit()
		result=db.session.query(User).all()[0]
		self.assertEqual(user.age,result.age,msg="实际结果不符合预期结果")
	def	test_3(self):
		user=User('baochangping',age=24)
		db.session.add(user)
		db.session.commit()
		result=db.session.query(User).all()[0]
		self.assertEqual(user.age,result.age,msg="实际结果不符合预期结果")
if __name__ == '__main__':
		unittest.main()
