from flask import render_template, request
from app import app
from models.event import Event
from models.event_list import add_new_event, events

@app.route('/events')
def index():
    return render_template('index.html', title="Events", events=events)

@app.route('/addevent', methods=['POST'])
def add_event():
    print(request.form)
    event_date = request.form["date"]
    event_name = request.form["name"]
    event_guests = request.form["guests"]
    event_location = request.form["location"]
    event_description = request.form["description"]
    print(request.form["recur"])

    if "recur" in request.form:
        event_recurring = request.form["recur"]
    else:
        event_recurring = request.form["name"]
    
    # event_recurring = request.form["recur"]

    new_event = Event(event_date, event_name, event_guests, event_location, event_description, event_recurring )
    add_new_event(new_event)

    # print(new_event)

    return render_template('index.html', title='Events', events=events)