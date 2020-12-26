from repository import UserRepository
from repository.mongo import MongoUserRepository


class UserService(object):
    def __init__(self, repo_client=UserRepository(adapter=MongoUserRepository)):
        self.repo_client = repo_client

    def find_user(self, user_id):
        return self.repo_client.find(user_id)

    def create_user(self, user_id):
        return self.repo_client.create(user_id)

    def update_apikey(self, body):
        return self.repo_client.update( body)

    def delete_user(self, user_id):
        return self.repo_client.delete(user_id)

    def find_key(self,key):
        return self.repo_client.find_key(key)
