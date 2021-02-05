from flask import Flask, request
from flask_cors import CORS
from db import Database

app = Flask(__name__)
db = Database()
CORS(app)

@app.route('/get', methods=['POST'])
def getLink():
    if 'url' in request.args:
        url = request.args['url']
    else:
        return {
            'status': 'fail'
        }

    if(db.checkURL(url)):
        link = db.getLink(url)

        return {
            'status': 'fail',
            'response': link
        }
    else:
        return {
            'status': 'fail'
        }


@app.route('/add', methods=['POST'])
def addURL():
    if 'url' in request.args:
        url = request.args['url']
    else:
        return {
            'status': 'fail'
        }

    if(db.checkURL(url)):
        link = db.getLink(url)

        return {
            'status': 'fail',
            'response': link
        }
    else:
        link = db.addURL(url)

        return {
            'status': 'success',
            'response': link
        }