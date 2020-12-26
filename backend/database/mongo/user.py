import datetime

from . import db


class User(db.Document):
    userId = db.StringField(required=True, unique=True)
    apiKey = db.StringField(unique=True,null = True)

    meta = {
        'collection': 'users',
        'indexes': [
            'userId',
            'apiKey'
        ]

    }
