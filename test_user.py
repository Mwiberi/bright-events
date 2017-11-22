import unittest
from users import user

class userRegistrationTestCase(unittest.TestCase):
    def setUp(self):
        User=user(1, 2, 3, 4, 2)

    def test_typeOfFields(self):
        User=user(1, 2, 3, 4, 2)
        result=User.add_user(1, 2, 3, 4, 2)
        self.assertEquals("Invalid input. Enter character elements", result)
