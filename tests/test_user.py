import unittest

from app.users import User
from app.users import Login
import views

class userRegistrationDetailsTestCase(unittest.TestCase):
    def setUp(self):
        self.myUser=User(1, 2, 3, 4, 2)

    def test_typeOfFields(self):
        result=self.myUser.create_user(1, 2, 3, 4, 2)
        self.assertEquals("Invalid input. Enter character elements", result)
    def test_emptyFields(self):
        result=self.myUser.create_user("", "","" , "", "")
        self.assertEquals("Kindly fill out all the form fields", result)
    def test_lengthPasswordLessThanEightCharacters(self):
        result=self.myUser.create_user("sue", "smith","sue" , "sue@outlookcom", "vg")
        self.assertEquals("Password length too small", result)



    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    def register(self, email, password, confirm):
    return self.app.post(
        '/brightEvents/api/v1/auth/register',
        data=dict(email=email, password=password, confirm=confirm),
        follow_redirects=True)
 


#class for checking the user details on the login page
class userLoginTestCase(unittest.TestCase):
    def setUp(self):
        self.myUser=Login()
    def test_loginDetailIfTheyExist(self):
        result=self.myUser.login_user("", "joe")
        self.assertEquals("Kindly fill out all the form fields", result)
    def login(self, email, password):
    return self.app.post(
        '/brightEvents/api/v1/auth/login',
        data=dict(uname=uname, pwd=pwd),
        follow_redirects=True)
 
    def logout(self):
    return self.app.get(
        '/brightEvents/api/v1/auth/logout',
        follow_redirects=True)

