import unittest

from users import User
from users import Login

class userRegistrationDetailsTestCase(unittest.TestCase):
    def setUp(self):
        self.myUser=user(1, 2, 3, 4, 2)

    def test_typeOfFields(self):
        result=self.myUser.add_user(1, 2, 3, 4, 2)
        self.assertEquals("Invalid input. Enter character elements", result)
    def test_emptyFields(self):
        result=self.myUser.add_user("", "","" , "", "")
        self.assertEquals("Kindly fill out all the form fields", result)
    def test_lengthPasswordLessThanEightCharacters(self):
        result=self.myUser.add_user("sue", "smith","sue" , "sueoulookcom", "vg")
        self.assertEquals("Password length too small", result)

#class for checking the user details on the login page
class userLoginTestCase(unittest.TestCase):
    def setUp(self):
        self.myUser=login()
    def test_loginDetailIfTheyExist(self):
        result=self.myUser.login_user("", "joe")
        self.assertEquals("Kindly fill out all the form fields", result)
    #def test_checkIfUserExistsInTheUsersMemory(self):

