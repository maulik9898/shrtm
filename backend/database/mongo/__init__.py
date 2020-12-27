import os
import urllib.parse

from flask_mongoengine import MongoEngine

db = MongoEngine()


def initialize_db(app):
    '''
    id = os.getenv('id')
    p = os.getenv('pass')
    h = os.getenv('MONGO_URI')
    h = h.replace('[:id]', urllib.parse.quote_plus(id))
    h = h.replace('[:pass]', urllib.parse.quote_plus(p))
    '''
    app.config['MONGODB_DB'] = 'db'
    app.config['MONGODB_HOST'] = 'db'
    app.config['MONGODB_PORT'] = 27017
    app.config['MONGODB_USERNAME'] = 'admin'
    app.config['MONGODB_PASSWORD'] = '1234567'
    db.init_app(app)
