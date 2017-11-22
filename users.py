class user(object):

    def __init__(self,fname, lname,uname,email,pwd):
        
        self.fname = fname
        self.lname =lname
        self.uname =uname
        self.email =email
        self.pwd = pwd

        details={}
        loginDetails={}
        

    def add_user(self,fname, lname,uname,email,pwd):
        self.fname = fname
        self.lname =lname
        self.uname =uname
        self.email =email
        self.pwd = pwd
        if fname and lname and uname and email and pwd:
            if type(fname) or type(name) or type(uname) or type(email) !=str:
                return "Invalid input. Enter character elements"
            
            elif len(pwd)<8:
                return("Password length too small")
            else:
                 #store details in a dictionary
                self.details={'Firstname':fname,'Lastname':lname,'Username':uname,'Email':email, 'Password':pwd}
                self.loginDetails[uname]=pwd
        else:
            return "Kindly fill out all the form fields"
  
class login(user):
    def login_user(self, uname, pwd):
        self.uname =uname
        self.pwd = pwd
        if uname and pwd:
            return "login successful"
        else:
            return"Kindly fill out all the form fields"
    def logout_user(self, uname):
        self.uname =uname
        session.delete()
        return "successfully logged out"
