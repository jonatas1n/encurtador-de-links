from flask import Flask, request
from flask_cors import CORS
import base64
import requests
from urllib.parse import urlparse

from db import Database

app = Flask(__name__)
CORS(app)
db = Database()

@app.route('/create', methods=['POST'])
def create():
    db.create()
    
    return {
        'status':'success'
    }

@app.route('/redirect', methods=['POST'])
def getUrl():
    link = request.args['link']

    url = db.getUrl(link)
    if(url):
        return {
            'status': 'success',
            'response': url
        }
    else:
        return {
            'status': 'fail',
            'response': ''
        }
        

@app.route('/get', methods=['POST'])
def getLink():
    if 'url' in request.args:
        url = request.args['url']
        parse = urlparse(url)
        url = url.replace(parse.scheme + '://', '')
        url = url.replace('www.', '')
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
    url = request.args['url']
    parse = urlparse(url)
    
    if parse.path == 'localhost:3000':
        return {
            'status': 'error'
        }

    url = url.replace(parse.scheme + '://', '')
    url = url.replace('www.', '')

    short = None
    
    if 'short' in request.args:
        short = request.args['short']

    if db.checkURL(url):
        link = db.getLink(url)

        return {
            'status': 'error',
            'response': link
        }
    elif urlValidate(url):
        short = db.addURL(url, short)

        return {
            'status': 'success',
            'response': short
        }
    else:
        return {
            'status': 'error'
        }

@app.route('/rank', methods=['GET'])
def getRank():
    result = db.getRank()

    response = []

    for i in range(len(result)):
        response.append(result[i])

    return {
        'status': 'success',
        'response': response
    }

def urlValidate(url):
    return True
    try:
        response = requests.get(url)
        print(response)
        return True
    except:
        return False

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)