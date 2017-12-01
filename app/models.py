import re


class User(object):
    #users list will be used to store a list of dictionaries for user accounts
    users = [
    {
        'userID': 1,
        'fname': 'sue',
        'lname': 'smith',
        'uname': 'sue', 
        'email': 'sue@outlook.com',
        'pwd': 'sue',
        'cpwd' :'sue'

    },
    {
        'userID': 2,
        'fname': 'sam',
        'lname': 'smith',
        'uname': 'sam', 
        'email': 'sam@outlook.com',
        'pwd': 'sam'
    }
]
    def __init__(self,fname, lname,uname,email,pwd, cpwd):
        self.fname = fname
        self.lname =lname
        self.uname =uname
        self.email =email
        self.pwd = pwd
        self.cpwd= cpwd

        

    def create_user(self,fname, lname,uname,email,pwd):
        
        if fname and lname and uname and email and pwd:
            if type(fname) or type(name) or type(uname) !=str:
                return "Invalid input. Enter character elements"
            
            elif len(pwd) <= 7:
                return("Password length too small")
            elif re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) == None:
                return "Enter a valid email address"
            elif pwd != cpwd:
                return('Passwords must match')
            else:
                 #store details in a dictionary
                self.users.append = ({'fname':fname,'lname':lname,'uname':uname,'email':email, 'pwd':pwd})
            
        else:
            return "Kindly fill out all the form fields"

  
    def login_user(self, uname, pwd):
        if not uname and pwd:
            return "Kindly fill out all the form fields"
        user = [user for user in users if user['uname'] == request.form['uname'] and user['pwd'] == request.form['pwd']]
        if len(user)>0:
            session['logged_in'] = True
        else:
            return 'Wrong username or password'

              
            
    def user_logout():
        session['logged_in'] = True 
        return "successfully logged out"

class Event(object):
    #dummy data for events
    #Also where the events created will be stored 
    events[
        {
        'eventName': 'Coke studio Africa',
        'eventID': 1,
        'location': 'Nairobi', 
        'date': '12-13-2017'

    },
    {
        'eventName': 'Don Moen concert',
        'eventID': 2,
        'location': 'Citam', 
        'date': '11-12-2017'

    }
    ]

    def __init__(self,eventName, eventID,location,date):
        
        self.eventName  = eventName
        self.eventID    =eventID
        self.location   =location
        self.date       =date
        
        

    def create_event(self):
        
        if type(name) or type(location) !=str:
            return "Invalid input. Enter character elements"
        if name and eventID and location and date:
            print(">>>>", )
            #store details in a dictionary
            self.eventDetails={'Event Name':name,'Event ID':eventID,'Location':location,'Date':date}
    def update_event(self, eventID):
        if type(eventID)!= int:
            return 'Invalid event ID. Event ID should be a number'
        
    def delete_event(self, eventID):
        if type(eventID)!= int:
            return 'Invalid event ID. Event ID should be a number'
        
    def retrieve_event(self, eventID):
        if type(eventID)!= int:
            return 'Invalid event ID. Event ID should be a number'
    def RSVP_event(self, eventID):
        if type(eventID)!= int:
            return 'Invalid event ID. Event ID should be a number'

    def view_eventGuests(self, eventID):
        if type(eventID)!= int:
            return 'Invalid event ID. Event ID should be a number'
