import datetime

from . import db


class ShortUrl(db.Document):
    slug = db.StringField(required=True, primary_key=True)
    originalUrl = db.StringField(required=True)
    visits = db.IntField(default=0)
    password = db.StringField()
    createdAt = db.DateTimeField(default=datetime.datetime.utcnow)

    meta = {
        'collection': 'shorturl',
        'auto_create_index': False,

    }
