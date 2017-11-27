#!flask/bin/python
from flask import Flask, jsonify 
from flask import Flask, flash, redirect, render_template, request, session, abort, make_response 



app = Flask(__name__)

events = [
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
#Function to create new events
@app.route('/brightEvents/api/v1/events', methods=['GET','POST'])
def create_events():
    if request.method == 'GET':
        #return render_template('userEvents.html', result= jsonify(events)) 
        return jsonify(events), 201
    else:

        if not request.json or not 'eventName' in request.json:
            abort(400)
            return render_template('index.html')
            event = {
        'eventID': events[-1]['id'] + 1,
        'eventName': request.json['eventName'],
        'location': request.json['location'],
        'date': request.json['date']
    }
        events.append(event)
        flash('Event added successfully')
        #return render_template('userEvents.html', result=jsonify({'event': event}))
        return jsonify(events), 201
    

# Function to the get event based on the ID
@app.route('/brightEvents/api/v1/events/<int:eventID>', methods=['GET'])
def get_event(eventID):
    event = [event for event in events if event['eventID'] == eventID]
    if len(event) == 0:
        abort(404)
    return render_template('userEvents.html', result=events) 

#creating a much better error 404 response
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Error': 'Not found'}), 404)

#Function to update an event
@app.route('/brightEvents/api/v1/events/<int:eventID>', methods=['PUT'])
def update_event(eventID):
    event = [event for event in events if event['eventID'] == eventID]
    if len(event) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'eventName' in request.json and type(request.json['eventName']) != unicode:
        abort(400)
    if 'location' in request.json and type(request.json['location']) is not unicode:
        abort(400)
    
    event[0]['eventName'] = request.json.get('eventName', event[0]['eventName'])
    event[0]['location'] = request.json.get('location', event[0]['location'])
    event[0]['date'] = request.json.get('date', event[0]['date'])
    return jsonify({'event': event[0]})


#Function to delete an event based on the ID
@app.route('/brightEvents/api/v1/events/<int:eventID>', methods=['DELETE'])
def delete_event(eventID):
    event = [event for event in events if event['eventID'] == eventID]
    if len(event) == 0:
        abort(404)
    event.remove(event[0])
    return jsonify({'result': True})


#Function to rsvp to an event
@app.route('/brightEvents/api/v1/events/<int:eventID>/rsvp', methods=['POST'])
def send_reply():
    pass


    # The main method
if __name__ == '__main__':
    app.run(debug=True)