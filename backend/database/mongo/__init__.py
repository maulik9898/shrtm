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
    db_name = os.environ.get('MONGODB_DB')
    host_name = os.environ.get('MONGO_URI')
    user_name = os.environ.get('MONGODB_USERNAME')
    password = os.environ.get('MONGODB_PASSWORD')
    host_name = host_name.replace('[:id]', urllib.parse.quote_plus(user_name))
    host_name = host_name.replace('[:pass]', urllib.parse.quote_plus(password))
    print(host_name)
    app.config['MONGODB_SETTINGS'] = {
        'host': host_name+'/'+db_name,
    }

    db.init_app(app)
