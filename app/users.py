
#!flask/bin/python
from flask import Flask, jsonify

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

#unction to create a new user
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
if __name__ == '__main__':
    app.run(debug=True)