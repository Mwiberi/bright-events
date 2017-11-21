class user(object):

    def __init__(fname, lname,uname,email,pwd):
        
        self.fname = fname
        self.lname =lname
        self.uname =uname
        self.email =email
        self.pwd = pwd
        

    def add_user(self,fname, lname,uname,email,pwd):
        self.fname = fname
        self.lname =lname
        self.uname =uname
        self.email =email
        self.pwd = pwd

    def login_user(self, uname, pwd):
        self.uname =uname
        self.pwd = pwd
    def logout_user(self, uname):
        self.uname =uname
