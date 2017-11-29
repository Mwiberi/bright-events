import unittest

from events import Event

class eventsCreation(unittest.TestCase):
    def setUp(self):
        eve=event(1, 2, 3, 4)

    def test_typeOfFields(self):
        eve=event(1, 2, 3, 4)
        result=eve.add_event(1, 2, 3, 4)
        self.assertEquals("Invalid input. Enter character elements", result)
