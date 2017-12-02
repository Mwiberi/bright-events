import unittest

from app.models import User, Event


class userRegistrationDetailsTestCase(unittest.TestCase):
    def setUp(self):
        self.myUser=User(self,1, 2, 3, 4, 2)

    def test_emptyFields(self):
        result=self.myUser.create_user("", "","" , "", "", "")
        self.assertEquals("Kindly fill out all the form fields", result)
    def test_lengthPasswordLessThanEightCharacters(self):
        result=self.myUser.create_user("sue", "smith","sue" , "sue@outlookcom", "vg","vg")
        self.assertEquals("Password length too small", result)
    def test_emailFormat(self):
        result=self.myUser.create_user("sue", "smith","sue" , "sueoutlookcom", "vnbnjncxjhjhg", "ahGSFBJNd")
        self.assertEquals("Enter a valid email address", result)
    def test_passwordMatch(self):
        result=self.myUser.create_user("sue", "smith","sue" , "sue@outlook.com", "vnbnjncxjhjhg", "ahGSFBJNd")
        self.assertEquals("Passwords must match", result)
    def test_loginDetails(self):
        result=self.myUser.login_user("", "")
        self.assertEquals("Kindly fill out all the form fields", result)
    def test_loginDetails(self):
        result=self.myUser.reset_password("", "", "")
        self.assertEquals("Kindly fill out all the form fields", result)
