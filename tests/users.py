class User(object):
    #details list will be used to store a list of dictionaries for user accounts
    details=[]
    def __init__(self,fname, lname,uname,email,pwd):
        self.fname = fname
        self.lname =lname
        self.uname =uname
        self.email =email
        self.pwd = pwd

        

    def create_user(self,fname, lname,uname,email,pwd):
        self.fname = fname
        self.lname =lname
        self.uname =uname
        self.email =email
        self.pwd = pwd
        if fname and lname and uname and email and pwd:
            if type(fname) or type(name) or type(uname) !=str:
                return "Invalid input. Enter character elements"
            
            elif len(pwd) <= 7:
                return("Password length too small")
            else:
                 #store details in a dictionary
                self.details.append=({'Firstname':fname,'Lastname':lname,'Username':uname,'Email':email, 'Password':pwd})
            
        else:
            return "Kindly fill out all the form fields"
  
class login(user):
    details=user.details
    
    def __init__(self):
        user.__init__(self)
    def login_user(self, uname, pwd):
        self.uname =uname
        self.pwd = pwd
        if not uname and pwd:
            return"Kindly fill out all the form fields"
        for detail in details:
            newUname= name.get('Username')
            newPwd = name.get('pwd')
            if newUname and newPwd:
                return "login successful"
            else:
                return "username or Password incorrect"
            
    def logout_user(self, uname):
        self.uname =uname
        session.delete()
        return "successfully logged out"
