#!flask/bin/python
from flask import Flask, jsonify
from flask import Flask, flash, redirect, render_template, request, session, abort, make_response, Markup
from flask_httpauth import HTTPBasicAuth
from models import User, Event, Guest
import re

# create an object of HTTPBasicAuth
auth = HTTPBasicAuth()
#declare instances of the classes
User=User(1, 2, 3, 4, 5, 6)
Event=Event(1, 2, 3, 4)
Guest=Guest(1, 2, 3, 4, 5, 6)

app = Flask(__name__)
app.secret_key = "superdooper1"

#/////////////////////////USER SIDE////////////////////////////

# Function to create a new user


@app.route('/brightEvents/api/v1/auth/register', methods=['GET', 'POST'])
def create_users():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        uname = request.form.get('uname')
        email = request.form.get('email')
        pwd = request.form.get('pwd')
        cpwd = request.form.get('cpwd')
        
        user=User.create_user(fname, lname, uname, email, pwd, cpwd)
        flash('Thanks for signing up please login')
        return render_template('user_login.html'), 200
        # return jsonify(users), 201
    return render_template('user_registration.html')


# Function to get the user login details and user login form if they are
# correct
@app.route('/brightEvents/api/v1/auth/login', methods=['GET', 'POST'])
#@auth.login_required
@auth.get_password
def getLoginDetails():
    if request.method == 'POST':
        uname = request.form['uname']
        pwd = request.form['pwd']
        user= User.login_user(uname, pwd)
    else:
        return render_template('user_login.html')


# Function to access the home page
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('events.html', result=Event.events)
    else:
        return render_template('index.html')


# make a better eror 401 response
@auth.error_handler
def unauthorized():
    return make_response(
        jsonify({'error': 'Unauthorized!Incorrect username or password'}), 401)


# The logout Function
@app.route('/brightEvents/api/v1/auth/logout')
def user_logout():
    session['logged_in'] = False
    return home()


# The Reset Password Function
@app.route('/brightEvents/api/v1/auth/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        opwd = request.form['opwd']
        npwd = request.form['npwd']
        cpwd = request.form['cpwd']
        reset=User.reset_password(opwd,npwd,cpwd)
#///GET///
    return render_template('reset_password.html')

    #////////////////////EVENTS SIDE/////////////////////////////////

# Functions to create new events


@app.route('/brightEvents/api/v1/events', methods=['GET', 'POST'])
def create_events():
    if request.method == 'POST':
        if not session.get('logged_in'):
            flash('You need to login to create an event')
            return render_template('user_login.html'), 401
        eventName = request.form['eventName']
        location = request.form['location']
        date = request.form['date']
        eve=User.create_event(eventName, location, date)

    return get_allEvents()


# Function to get all the events
@app.route('/brightEvents/api/v1/events', methods=['GET'])
def get_allEvents():
    return render_template('userEvents.html', result=Event.events)
    # return jsonify(events), 201 --. would apply if the api was not connected
    # to the templates


# Function to the get event based on the ID
@app.route('/brightEvents/api/v1/events/<int:eventID>', methods=['GET'])
def get_event(eventID):
    event = [event for event in Event.events if event['eventID'] == eventID]
    if len(event) == 0:
        abort(404)
    # results=[]
    # results.append(event)
    # return jsonify(results)
    return render_template('userEvents.html', result=event)

# creating a much better error 404 response


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Error': 'Not found'}), 404)

# Function to update an event


@app.route('/brightEvents/api/v1/events/<int:eventID>', methods=['PUT'])
def update_event(eventID):
    event = [event for event in Event.events if event['eventID'] == eventID]
    if len(event) == 0:
        abort(404)
    # if type(request.form['eventName']) is not str:
        # abort(400)
    # if type(request.form['location']) is not str:
        # abort(400)

    event[0]['eventName'] = request.form.get(
        'eventName', event[0]['eventName'])
    event[0]['location'] = request.form.get('location', event[0]['location'])
    event[0]['date'] = request.form.get('date', event[0]['date'])
    # return jsonify({'event': event[0]})
    return jsonify(Event.events), 201  # code for updated successfully


# creating a much better error 400 response
@app.errorhandler(400)
def bad_request(error):
    return make_response(
        jsonify({'Error': 'Details entered are incorrect'}), 400)

# Function to delete an event based on the ID


@app.route('/brightEvents/api/v1/events/<int:eventID>', methods=['DELETE'])
def delete_event(eventID):
    event = [event for event in Event.events if event['eventID'] == eventID]
    if len(event) == 0:
        abort(404)
        return jsonify({'Message': 'Event specified does not exist'}), 404
    events.remove(event[0])
    # return jsonify(events)--- would apply for postman/not using templates
    return render_template('userEvents.html', result=Event.events)


# Function to rsvp to an event
@app.route(
    '/brightEvents/api/v1/events/<int:eventID>/rsvp',
    methods=[
        'GET',
        'POST'])
def rsvp(eventID):
    event = [event for event in Event.events if event['eventID'] == eventID]
    if len(event) == 0:
        abort(404)
    if request.method == 'POST':
        '''
        user = [user for user in users if user['uname'] == uname]
        if len(user) == 0:
            abort(404)
        eventID=event[0]['eventID']
        uname=user['uname']
        email=user['email']
        userID=user[0]['userID']
        reply=request.form('reply')
        guest={
            'eventID':eventID,
            'uname' :uname,
            'email' :email,
            'userID':userID,
            'reply' :reply

            }
        guests.append(guest)
        return 'You have sent your rsvp'
        return jsonify(guests)
        #return render_template('events.html', event = event)'''

        eventID = event[0]['eventID']
        eventName = event[0]['eventName']
        uname = request.form['uname']
        email = request.form['email']
        reply = request.form['reply']

        guest = Guest.rsvp(uname, email, reply, eventName, eventID)
    ###GET##
    return render_template('rsvp.html', eventID=eventID)


# Function to get all guests
@app.route('/brightEvents/api/v1/events/guests', methods=['GET'])
def getGuests():
    return render_template('guests.html', result=Guest.guests)



    # The main method
if __name__ == '__main__':
    app.run(debug=True)
