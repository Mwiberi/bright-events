import unittest

from app.models import Event, Guest

class eventsCreation(unittest.TestCase):
    def setUp(self):
        self.eve=Event(1, 2, 3, 4)
        self.eve1=Guest(1, 2, 3, 4, 5, 7)

    def test_test_emptyFields(self):
        result=self.eve.create_event("", "","")
        self.assertEquals("All fields must be filled in", result)
    def test_typeEventID(self):
        result=self.eve.update_event("bvgf")
        self.assertEquals('Invalid event ID. Event ID should be a number', result)
    def test_rsvpDetails(self):
        result=self.eve1.rsvp("", "", "", "", "")
        self.assertEquals("Kindly fill out all the form fields", result)
    def test_rsvpEmail(self):
        result=self.eve1.rsvp("sdfSF", "SDFSDF", "SFSDGF", "DFDSG", "DGBB")
        self.assertEquals("Enter a valid email address", result)

