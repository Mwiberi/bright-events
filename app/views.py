#!flask/bin/python
from flask import Flask, jsonify 
from flask import Flask, flash, redirect, render_template, request, session, abort, make_response, Markup 
from flask_httpauth import HTTPBasicAuth

#create an object of HTTPBasicAuth
auth=HTTPBasicAuth()




app = Flask(__name__)
app.secret_key = "superdooper1"
users = [
    {
        'userID': 1,
        'fname': 'sue',
        'lname': 'smith',
        'uname': 'sue', 
        'email': 'sue@outlook.com',
        'pwd': 'sue',
        'cpwd' :'sue'

    },
    {
        'userID': 2,
        'fname': 'sam',
        'lname': 'smith',
        'uname': 'sam', 
        'email': 'sam@outlook.com',
        'pwd': 'sam'
    }
]

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
#/////////////////////////USER SIDE////////////////////////////

#Function to create a new user
@app.route('/brightEvents/api/v1/auth/register', methods=['GET', 'POST'])
def create_users():
    if request.method == 'POST':

        user = {
            'userID': users[-1]['userID'] + 1,
            'fname': request.form['fname'],
            'lname': request.form['lname'],
            'uname': request.form['uname'],
            'email': request.form['email'],
            'pwd': request.form['pwd'],
            'cpwd': request.form['cpwd']
    }
        users.append(user)
        flash('Thanks for signing up please login')
        return render_template('user_login.html')
        #return jsonify(users)
    return render_template('user_registration.html')
   
        


#Function to get the user login details and user login form if they are correct
@app.route('/brightEvents/api/v1/auth/login', methods=['GET','POST'])
#@auth.login_required
@auth.get_password
def getLoginDetails():
    if request.method == 'POST':
        user = [user for user in users if user['uname'] == request.form['uname'] and user['pwd'] == request.form['pwd']]
        if len(user) >= 1:
            session['logged_in'] = True
        else:
            flash('Wrong username or password')
        return home()
    return render_template('user_login.html')


#Function to access the home page
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('user_login.html')
    else:
        return render_template('index.html')  
             
   

# make a better eror 401 response
@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized!Incorrect username or password'}), 401)



   
#The logout Function
@app.route('/brightEvents/api/v1/auth/logout')
def user_logout():
    session['logged_in'] = False
    return home()



    #////////////////////EVENTS SIDE/////////////////////////////////
    
#Functions to create new events
@app.route('/brightEvents/api/v1/events', methods=['GET','POST'])
def create_events():
    if request.method == 'POST':
        if not 'eventName':
            message = Markup("All fields must be filled")
            flash(message)
            return render_template('index.html'), 400
   
        event = {
            'eventID': events[-1]['eventID'] + 1,
            'eventName': request.form['eventName'],
            'location': request.form['location'],
            'date': request.form['date']
        }
        events.append(event)
        flash('Event added successfully')
        return render_template('userEvents.html', result=events)
        #return jsonify(events), 201 -----would apply if the api was not connected to the templates
    return get_allEvents()




#Function to get all the events
@app.route('/brightEvents/api/v1/events',methods=['GET'])
def get_allEvents():
    return render_template('userEvents.html', result= events) 
    #return jsonify(events), 201 --. would apply if the api was not connected to the templates

    

# Function to the get event based on the ID
@app.route('/brightEvents/api/v1/events/<int:eventID>', methods=['GET'])
def get_event(eventID):
    event = [event for event in events if event['eventID'] == eventID]
    if len(event) == 0:
        abort(404)
    results=[]
    results.append(event)
    #return jsonify(results)
    return render_template('userEvents.html', result=results)

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
    