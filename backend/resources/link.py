from flask import Response, request
from flask_restful import Resource
from bson import json_util

from auth import check_apiKey
from service.linkservice import LinkService
from auth.middleware.firebase import check_token
from utils.utils import *
import json

api = LinkService()


class LinkApi(Resource):

    @check_apiKey
    @check_token
    def get(self, slug):
        resp, code = api.find_url(slug)
        return Response(json.dumps(resp,default=json_util.default), mimetype="application/json", status=code)

    @check_apiKey
    @check_token
    def post(self):
        body = request.get_json()
        body['userId'] = request.user['userId']
        if not body.get('slug'):
            c = 200
            slug = generate_random_key(7)
            while c != 200:
                slug = generate_random_key(7)
                r, c = api.find_url(slug)
            body['slug'] = slug

        resp, code = api.create_short_url(body)

        return Response(json.dumps(resp,default=json_util.default), mimetype="application/json", status=code)

    @check_apiKey
    @check_token
    def put(self, slug):
        body = request.get_json()
        body['userId'] = request.user['userId']
        resp, code = api.update_short_url(slug, body)
        return Response(json.dumps(resp,default=json_util.default), mimetype="application/json", status=code)

    @check_apiKey
    @check_token
    def delete(self, slug):
        user_id = request.user['userId']
        resp, code = api.delete_short_url(slug,user_id)
        return Response(json.dumps(resp,default=json_util.default), mimetype="application/json", status=code)

    def options(self):
        resp = ''
        code = 200
        return Response(json.dumps(resp,default=json_util.default), mimetype="application/json", status=code)
