import json

from mongoengine import Q
from mongoengine.errors import *

from database.mongo.shorturl import ShortUrl
from database.mongo.user import User


class MongoShortUrlRepository(object):

    def find(self, slug):
        try:
            short_url = ShortUrl.objects.get(slug=slug).to_mongo().to_dict()
            status_code = 200
            del short_url['_id']
            del short_url['userId']
        except DoesNotExist:
            short_url = {'slug': slug, 'error': "Slug not found"}
            status_code = 404
            return short_url, status_code

        return short_url, status_code

    def create(self, short_link):
        status_code = 200
        try:
            short_url = ShortUrl(**short_link).save(force_insert=True).to_mongo().to_dict()
            del short_url['_id']
            del short_url['userId']
        except Exception as e:
            short_url = {'slug': short_link['slug'], 'error': "Slug already present"}
            status_code = 409

        return short_url, status_code

    def update(self, slug, body):
        if body.get('slug'):
            del body['slug']
        try:
            updated_fields = ShortUrl.objects.get(Q(slug=slug) & Q(userId=body['userId'])).update(**body)
            if updated_fields == 0:
                short_url = {'slug': slug, 'error': "Error updating slug"}
                status_code = 404
            else:
                short_url, status_code = self.find(slug)
        except DoesNotExist:
            short_url = {'slug': slug, 'error': "Slug not found"}
            status_code = 404

        return short_url, status_code

    def delete(self, slug,user_id):
        try:
            deleted_field = ShortUrl.objects.get(Q(slug=slug) & Q(userId=user_id)).delete()
            short_url = {'slug': slug, 'message': "Slug deleted"}
            status_code = 200
        except DoesNotExist:
            short_url = {'slug': slug, 'error': "Slug not found"}
            status_code = 404
        return short_url, status_code


class MongoUserRepository(object):

    def find(self, user_id):
        try:
            user = User.objects.get(userId=user_id).to_mongo().to_dict()
            del user['_id']
        except DoesNotExist:
            user = None

        return user

    def create(self, user):
        try:
            user = User(**user).save(force_insert=True).to_mongo().to_dict()
            del user['_id']
        except:
            user = None

        return user

    def update(self, body):
        try:
            updated_fields = User.objects.get(userId = body['userId']).update(apiKey=body['apiKey'])
            user = self.find(body['userId'])
        except DoesNotExist:
            user = None
        return user

    def delete(self, slug):
        pass

    def find_key(self,key):
        try:
            user = User.objects.get(apiKey=key).to_mongo().to_dict()
            del user['_id']
        except DoesNotExist:
            user = None

        return user


