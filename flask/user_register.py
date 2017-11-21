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

@app.route('/brightEvents/api/auth/register', methods=['GET'])
def get_users():
    return jsonify({'users': users})

if __name__ == '__main__':
    app.run(debug=True)