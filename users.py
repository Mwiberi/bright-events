class user(object):

    def __init__(self,fname, lname,uname,email,pwd):
        
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
        if type(fname) or type(name) or type(uname) or type(email)!=str:
            return "Invalid input. Enter character elements"
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
