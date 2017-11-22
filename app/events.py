#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {
        'eventName': u'sue',
        'eventID': u'smith',
        'location': u'Nairobi', 
        'date': '12-13-2017'

    }
]

@app.route('/brightEvents/api/v1/auth/register', methods=['GET'])
def get_users():
    return jsonify({'users': users})

if __name__ == '__main__':
    app.run(debug=True)