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

        

    def create_user(self,fname, lname,uname,email,pwd, cpwd):
        if not fname or not lname or not uname or not email or not pwd:
            return('Kindly fill out all the form fields')
        elif len(pwd) <= 7:
            return("Password length too small")
        elif re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) == None:
            return("Enter a valid email address")
        elif pwd != cpwd:
            return('Passwords must match')
        else:
            #store details in a dictionary
            self.users.append = ({'fname':fname,'lname':lname,'uname':uname,'email':email, 'pwd':pwd})
            
    def login_user(self, uname, pwd):
        if not uname or not pwd:
            return("Kindly fill out all the form fields")

              
            
    def user_logout():
        session['logged_in'] = False 
        return "successfully logged out"

class Event(object):
    #dummy data for events
    #Also where the events created will be stored 
    events=[
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
        
        if not eventName or not location or not date:
            return "All fields must be filled in"
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
