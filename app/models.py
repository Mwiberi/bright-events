from flask import Flask, flash, redirect, render_template, request, session, abort, make_response, Markup
import re


class User(object):
    #users list will be used to store a list of dictionaries for user accounts
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
    guests=[{
    'uname':'John',
    'email':'smiles@gmail.com',
    'eventName':'Coke studio Africa',
    'eventID':1,
    'reply':'I will be attending'
    }
    ]
    def __init__(self,fname, lname,uname,email,pwd, cpwd):
        self.fname = fname
        self.lname =lname
        self.uname =uname
        self.email =email
        self.pwd = pwd
        self.cpwd= cpwd

        

    def create_user(self, fname, lname, uname, email, pwd, cpwd):
        if not fname or not lname or not uname or not email or not pwd:
            flash('Kindly fill out all the form fields')
            return render_template('user_registration.html'), 400
        elif len(pwd) <= 7:
            flash("Password length too small")
            return render_template('user_registration.html'), 400
        elif re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) == None:
            flash("Enter a valid email address")
            return render_template('user_registration.html'), 400
        elif pwd != cpwd:
            flash('Passwords must match')
            return render_template('user_registration.html'), 400
        else:
            user = {
            'userID': users[-1]['userID'] + 1,
            'fname': fname,
            'lname': lname,
            'uname': uname,
            'email': email,
            'pwd': pwd,

        }
        #store details in a dictionary
        self.users.append(user)
           
            
            
    def login_user(self, uname, pwd):
        if not uname or not pwd:
            flash("Kindly fill out all the form fields")
            user = [user for user in self.users if user['uname'] == uname and user['pwd'] == pwd]
            if len(user) >= 1:
                self.session['logged_in'] = True
                self.session['uname'] = request.form['uname']
                return render_template('index.html', result=self.session['uname']), 200
            else:
                flash('Wrong username or password')
                return render_template('user_login.html'), 401

    def reset_password(self, opwd,npwd,cpwd):
        user = [user for user in self.users if user['pwd'] == opwd]
        if len(user) == 0:
            flash('Old Password Incorrect')
            return render_template('reset_password.html'), 400
        elif not opwd or not npwd or not cpwd:
            flash('Kindly fill out all the form fields')
            return render_template('reset_password.html'), 400
        elif len(npwd) < 8:
            flash('Password length too short. Enter atleast 8 characters')
            return render_template('reset_password.html'), 400
        elif npwd != cpwd:
            flash('Passwords must match')
            return render_template('reset_password.html'), 400
        user[0]['pwd'] = request.form.get('npwd', user[0]['pwd'])
        # return jsonify({'user': user[0]})--shows the new details for the user
        # ie new password and the other details
        flash('Password successfully changed')
        return render_template('index.html'), 200


class Event(object):
    #dummy data for events
    #Also where the events created will be stored 
    events=[
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

    def __init__(self,eventName, eventID,location,date):
        
        self.eventName  = eventName
        self.eventID    =eventID
        self.location   =location
        self.date       =date
        
        

    def create_event(self, eventName, location, date):
        
        if not eventName or not location or not date:
            flash("All fields must be filled in")
            return render_template('index.html'), 400
            #store details in a dictionary
        event = {
            'eventID': events[-1]['eventID'] + 1,
            'eventName': eventName,
            'location': location,
            'date': date

        }
        self.events.append(event)
        flash('Event added successfully')
        return render_template('userEvents.html', result=self.events)
        # return jsonify(events), 201 -----would apply if the api was not
        # connected to the templates
    def update_event(self, eventID):
        if type(eventID)!= int:
            return 'Invalid event ID. Event ID should be a number'
        
    


class Guest(User, Event):
    guests=[{
    'uname':'John',
    'email':'smiles@gmail.com',
    'eventName':'Coke studio Africa',
    'eventID':1,
    'reply':'I will be attending'
    }
    ]

    def rsvp(self, uname, email, reply, eventName, eventID):
        if not uname or not email or not reply:
            flash('Kindly fill out all the form fields')
            return render_template('rsvp.html', eventID=eventID), 400
        elif re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) is None:
            flash("Enter a valid email address")
            return render_template('rsvp.html', eventID=eventID), 400
        guest = {
            'eventID': eventID,
            'eventName': eventName,
            'uname': uname,
            'email': email,
            'reply': reply
        }
        self.guests.append(guest)
        flash('You have sent your rsvp')
        # return jsonify(guests)
        return render_template('events.html', result=self.events)