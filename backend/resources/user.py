import json

from flask import Response, request
from flask_restful import Resource
from bson import json_util

from utils.utils import *
from auth.middleware.firebase import check_token
from service.userservice import UserService

api = UserService()


class UserApi(Resource):

    @check_token
    def get(self):
        user_id = request.user['uid']
        user = api.find_user(user_id)
        if not user:
            user = api.create_user({'userId': user_id})

        return Response(json.dumps(user, default=json_util.default), mimetype="application/json", status=200)

    @check_token
    def put(self):
        user_id = request.user['uid']
        key = generate_random_key(20)
        user = api.find_key(key)
        while user:
            key = generate_random_key(20)
            user = api.find_key(key)
        body = {
            'userId': user_id,
            'apiKey': key
        }
        user = api.update_apikey(body)
        return Response(json.dumps(user, default=json_util.default), mimetype="application/json", status=200)


    def options(self):
        resp = ''
        code = 200
        return Response(json.dumps(resp, default=json_util.default), mimetype="application/json", status=code)
