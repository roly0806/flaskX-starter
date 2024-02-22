from flask import Flask, abort, request
from flask_restx import Resource, Api, fields
from werkzeug.middleware.proxy_fix import ProxyFix
import json
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(
    app, version='1.0', 
    title='Flaskx Starter',
    description='A Flaskx Starter',
    doc='//api/docs/'
)

load_dotenv()
KEY = os.getenv('KEY')

ns = api.namespace('default', description='default')

@ns.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True, port=3000, host="0.0.0.0")