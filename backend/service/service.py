from repository import Repository
from repository.mongo import MongoRepository


class Service(object):
    def __init__(self, repo_client=Repository(adapter=MongoRepository)):
        self.repo_client = repo_client

    def find_url(self, slug):
        return self.repo_client.find(slug)

    def create_short_url(self, short_link):
        return self.repo_client.create(short_link)

    def update_short_url(self, slug, body):
        return self.repo_client.update(slug, body)

    def delete_short_url(self, slug):
        return self.repo_client.delete(slug)
