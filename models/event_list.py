from models.event import *

event1 = Event("14/04/22", "Wedding", 120, "Ballroom", "The marriage of Pam and Jim", True)
event2 = Event("25/12/22", "Christmas Lunch", 20, "Main Hall", "A special celebratory feast", False)

events = [event1, event2]

def add_new_event(event):
    events.append(event)