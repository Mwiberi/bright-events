
#!flask/bin/python
from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
#create an object of HTTPBasicAuth
auth=HTTPBasicAuth()



app = Flask(__name__)

users = [
    {
        'fname': u'sue',
        'lname': u'smith',
        'uname': u'sue', 
        'email': u'sue@outlook.com',
        'pwd': 'sue'

    },
    {
        'fname': u'sam',
        'lname': u'smith',
        'uname': u'sam', 
        'email': u'sam@outlook.com',
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
        'email': request.json['email']
        'pwd': request.json['pwd']
    }
    users.append(user)
    return jsonify({'user': user}), 201

#Function to get the user login details and user login if they are correct
@app.route('brightEvents/api/v1/auth/login', methods=['POST'])
@auth.login_required
@auth.get_LoginDetails
def getLoginDetails(uname,pwd):
user = [user for user in userss if user['uname'] == uname and user['pwd'] == pwd]
 if len(user) == 0:
        abort(401)
else:
    session.start() #starts a session for the logged in user
    return jsonify({'user': user[0]})

# make a better eror 401 response
@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorizd!Incorrect username or password'}), 401)

   
#The logout Function
@app.route('brightEvents/api/v1/auth/logout')
def user_logout():
    session.clear



 #The main method
if __name__ == '__main__':
    app.run(debug=True)