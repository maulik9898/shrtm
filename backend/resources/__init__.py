from .link import LinkApi
from .root import Root
from .user import UserApi

'''
import different routes and initialize here
'''


def initialize_routes(api):
    api.add_resource(LinkApi, '/api/link/<string:slug>', '/api/link/')
    api.add_resource(UserApi, '/api/user/')
    api.add_resource(Root, '/<slug>')
