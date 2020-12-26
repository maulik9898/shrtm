from repository import ShortUrlRepository
from repository.mongo import MongoShortUrlRepository


class LinkService(object):
    def __init__(self, repo_client=ShortUrlRepository(adapter=MongoShortUrlRepository)):
        self.repo_client = repo_client

    def find_url(self, slug):
        return self.repo_client.find(slug)

    def create_short_url(self, short_link):
        return self.repo_client.create(short_link)

    def update_short_url(self, slug, body):
        return self.repo_client.update(slug, body)

    def delete_short_url(self, slug,user_id):
        return self.repo_client.delete(slug,user_id)
