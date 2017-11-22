import unittest
from users import user

class userRegistrationTestCase(unittest.TestCase):
    def setUp(self):
        User=user()

    def test_typeOfFields(self):
        result=User.add_user(1, 2, 3, 4, 4)
        self.assertRaises(ValueError)
