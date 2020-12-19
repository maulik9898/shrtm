from .root import RootApi

'''
import different routes and initialize here
'''


def initialize_routes(api):
    api.add_resource(RootApi, '/api/<string:slug>', '/api/')
