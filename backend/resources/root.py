from flask import Response, request, redirect
from flask_restful import Resource
from bson import json_util

from service.linkservice import LinkService

api = LinkService()


class Root(Resource):

    def get(self, slug):
        res, code = api.find_url(slug)
        if code != 200:
            return f" url not found", code
        return redirect(res['originalUrl'], 302)

