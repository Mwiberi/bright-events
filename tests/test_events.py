import unittest

from app.models import Event

class eventsCreation(unittest.TestCase):
    def setUp(self):
        self.eve=Event(1, 2, 3, 4)

    def test_test_emptyFields(self):
        result=self.eve.create_event("", "","")
        self.assertEquals("All fields must be filled in", result)
    def test_typeEventID(self):
        result=self.eve.delete_event("bvgf")
        self.assertEquals('Invalid event ID. Event ID should be a number', result)
    def test_rsvpDetails(self):
        result=self.eve.rsvp_event("","","")
        self.assertEquals("Kindly fill out all the form fields", result)
