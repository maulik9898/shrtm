from functools import wraps

from flask import request

from service.userservice import UserService

api = UserService()


def check_apiKey(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if not request.headers.get('X-Api-Key'):
            request.user = None
            return f(*args, **kwargs)

        token = request.headers['X-Api-Key']
        user = api.find_key(token)
        if not user:
            return {'message': 'No valid token provided'}, 400
        request.user = user
        return f(*args, **kwargs)

    return wrap
