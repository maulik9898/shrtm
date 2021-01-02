from functools import wraps

from firebase_admin import auth
from flask import request, g


def check_token(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        try:
            if request.user:
                return f(*args, **kwargs)
        except AttributeError:
            pass
        if not request.headers.get('authorization'):
            return {'message': 'No valid token provided'}, 400
        try:
            token = request.headers['authorization'].split(' ')[1]
            user = auth.verify_id_token(token)
            request.user = user
            request.user['userId'] = user['uid']
        except:
            return {'message': 'Invalid token provided.'}, 400
        return f(*args, **kwargs)

    return wrap
