
#!flask/bin/python
from flask import Flask, jsonify
from flask import Flask, flash, redirect, render_template, request, session, abort, make_response 
from flask_httpauth import HTTPBasicAuth

#create an object of HTTPBasicAuth
auth=HTTPBasicAuth()


#create and instance of the Flask class
app = Flask(__name__)
app.secret_key = "superdooper"
users = [
    {
        'fname': 'sue',
        'lname': 'smith',
        'uname': 'sue', 
        'email': 'sue@outlook.com',
        'pwd': 'sue'

    },
    {
        'fname': 'sam',
        'lname': 'smith',
        'uname': 'sam', 
        'email': 'sam@outlook.com',
        'pwd': 'sam'
    }
]

#Function to create a new user
@app.route('/brightEvents/api/v1/auth/register', methods=['POST'])
def create_users():
    if not request.json or not 'uname' in request.json:
        abort(400)
        user = {
        'fname': request.json['fname'],
        'lname': request.json['lname'],
        'uname': request.json['uname'],
        'email': request.json['email'],
        'pwd': request.json['pwd']
    }
    users.append(user)
    return jsonify({'user': user}), 201

#Function to get the user login details and user login if they are correct
@app.route('/brightEvents/api/v1/auth/login', methods=['POST'])
#@auth.login_required
@auth.get_password
def getLoginDetails():
    user = [user for user in users if user['uname'] == request.form['uname'] and user['pwd'] == request.form['pwd']]
    if len(user) >= 1:
        session['logged_in'] = True
    else:
        flash('Wrong username or password')
    return home()

#Function to login the user
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
    



 #The main method
if __name__ == '__main__':
    app.run(debug=True)
    