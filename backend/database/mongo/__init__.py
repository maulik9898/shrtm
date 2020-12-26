import os
import urllib.parse

from flask_mongoengine import MongoEngine

db = MongoEngine()


def initialize_db(app):
    id = os.getenv('id')
    p = os.getenv('pass')
    h = os.getenv('MONGO_URI')
    h = h.replace('[:id]', urllib.parse.quote_plus(id))
    h = h.replace('[:pass]', urllib.parse.quote_plus(p))
    app.config['MONGODB_SETTINGS'] = {
        'db': 'shrtm',
       # 'host': h,
        'host': 'mongodb://127.0.0.1:27017/'
    }
    db.init_app(app)
