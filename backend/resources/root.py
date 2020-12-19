from flask_restful import Resource
from flask import Request, Response


class RootApi(Resource):
    def get(self):
        return Response('Hello world',status=200)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
