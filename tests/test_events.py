import unittest

from app.models import Event

class eventsCreation(unittest.TestCase):
    def setUp(self):
        self.eve=Event(1, 2, 3, 4)

    def test_typeOfFields(self):
        result=self.eve.create_event(1, 2, 3)
        self.assertEquals("Invalid input. Enter character elements", result)
    def test_test_emptyFields(self):
        result=self.eve.create_event("", "","")
        self.assertEquals("All fields must be filled in", result)
