import json

from mongoengine.errors import *

from database.mongo.shorturl import ShortUrl


class MongoRepository(object):
    def __init__(self):
        pass

    def find(self, slug):
        try:
            short_url = ShortUrl.objects.get(slug=slug)
            status_code = 200
        except DoesNotExist:
            short_url = {'slug': slug, 'error': "Slug not found"}
            status_code = 404
            return short_url, status_code

        return short_url, status_code

    def create(self, short_link):
        status_code = 200
        try:
            short_url = ShortUrl(**short_link).save(force_insert=True)
        except :
            short_url = {'slug': short_link['slug'], 'error': "Slug already present"}
            status_code = 409

        return short_url, status_code

    def update(self, slug, body):
        if body.get('slug'):
            del body['slug']
        try:
            updated_fields = ShortUrl.objects.get(slug=slug).update(**body)
            if updated_fields == 0:
                short_url = {'slug': slug, 'error': "Error updating slug"}
                status_code = 404
            else:
                short_url, status_code = self.find(slug)
        except DoesNotExist:
            short_url = {'slug': slug, 'error': "Slug not found"}
            status_code = 404

        return short_url, status_code

    def delete(self, slug):
        res = ShortUrl.objects(slug=slug).delete()
        short_url = json.dumps({'slug': slug, 'error': "Slug deleted"})
        status_code = 200
        return short_url, status_code
