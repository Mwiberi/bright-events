class user(object):

    def __init__(fname, lname,uname,email,pwd):
        
        self.fname = fname
        self.lname =lname
        self.uname =uname
        self.email =email
        self.pwd = pwd

        details={}
        

    def add_user(self,fname, lname,uname,email,pwd):
        self.fname = fname
        self.lname =lname
        self.uname =uname
        self.email =email
        self.pwd = pwd
        if fname and lname and uname and email and pwd:
            #store details in a dictionary
            self.details={'Firstname':fname,'Lastname':lname,'Username':uname,'Email':email, 'Password':pwd}

    def login_user(self, uname, pwd):
        self.uname =uname
        self.pwd = pwd
        if uname and pwd:
            return "login successful"
    def logout_user(self, uname):
        self.uname =uname
        return "successfully logged out"
