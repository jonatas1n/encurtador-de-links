from flask import Flask, request
from flask_cors import CORS
import base64
import requests
from urllib.parse import urlparse
import json

from db import Database

app = Flask(__name__)
CORS(app)
db = Database()

@app.before_request
def createInit():
    db.create()

@app.route('/', methods=['GET', 'POST'])
def showRoutes(): 
    return {
        'status': 'success',
        'response': {
            '/': {
                'description': 'Show all routes avaiable in API',
                'parameters': None
            },
            '/create' : {
                'description': 'Create addresses table in database if not already created',
                'parameters': None
            },
            '/check' : {
                'description': 'Returns true if a short link exists in DB',
                'parameters': {
                    'short': 'Short Link'
                }
            },
            '/redirect' : {
                'description': 'Redirects navigator from shorted link to corresponding url',
                'parameters': {
                    'link': 'Shorted link'
                }
            },
            '/add' : {
                'description': 'Add a row in table that contains a url, shorted link and another useful data',
                'parameters': {
                    'url' : 'URL to be shortened',
                    'short' : 'Custom text to use as shortened link. (Optional parameter)'
                }
            },
            '/rank' : {
                'descripion': 'Returns the five most accessed links from PetitLinks',
                'parameters': None
            }
        }
    }

@app.route('/add', methods=['GET', 'POST'])
def addURL():
    url = request.args['url']
    parse = urlparse(url)
    
    if 'petit.com' in parse.path:
        return {
            'status': 'error'
        }

    url = url.replace(parse.scheme + '://', '')
    url = url.replace('www.', '')

    short = None
    
    if 'short' in request.args:
        short = request.args['short']

    link = db.get_link(url)
    
    if link:
        return {
            'status': 'error',
            'response': link
        }
    else:
        db.add_url(url, short)
        link = db.get_link(url)
        return {
            'status': 'success',
            'response': link
        }

@app.route('/create', methods=['GET', 'POST'])
def create():
    db.create()
    
    return {
        'status':'success'
    }

@app.route('/check', methods=['GET', 'POST'])
def check_link():
    short = request.args['short']

    if db.get_url(short):
        return {
            'status':'success',
            'response': True
        }

    return {
        'status':'success',
        'response': False
    }

@app.route('/rank', methods=['GET'])
def getRank():
    result = db.get_rank()

    response = []

    for i in range(len(result)):
        response.append(result[i])

    return {
        'status': 'success',
        'response': response
    }

@app.route('/redirect', methods=['GET', 'POST'])
def getUrl():
    link = request.args['link']

    methods = ['not-found', 'show']
    if link in methods:
        return {
            'status': error
        }

    url = db.get_url(link)
    if(url):
        return {
            'status': 'success',
            'response': url
        }
    else:
        return {
            'status': 'error',
        }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)