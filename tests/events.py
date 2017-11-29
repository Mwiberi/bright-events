class Event(object):

    def __init__(self,name, eventID,location,date):
        
        self.name = name
        self.eventID =eventID
        self.location =location
        self.date =date
        

        self.event_details={}
        

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
