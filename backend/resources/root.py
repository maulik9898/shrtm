from flask import Response, request
from flask_restful import Resource

from service.service import Service

api = Service()


class RootApi(Resource):

    def get(self, slug):
        resp, code = api.find_url(slug)
        return Response(resp, mimetype="application/json", status=code)

    def post(self):
        body = request.get_json()
        resp, code = api.create_short_url(body)
        return Response(resp, mimetype="application/json", status=code)

    def put(self, slug):
        body = request.get_json()
        resp, code = api.update_short_url(slug, body)
        return Response(resp, mimetype="application/json", status=code)

    def delete(self, slug):
        resp, code = api.delete_short_url(slug)
        return Response(resp, mimetype="application/json", status=code)
