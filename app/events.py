class Event(object):
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
