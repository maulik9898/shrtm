class ShortUrlRepository(object):
    def __init__(self, adapter=None):
        if not adapter:
            raise ValueError("Invalid repository implementation")
        self.client = adapter()

    def find(self, slug):
        return self.client.find(slug)

    def create(self, short_link):
        return self.client.create(short_link)

    def update(self, slug, short_link):
        return self.client.update(slug, short_link)

    def delete(self, slug,user_id):
        return self.client.delete(slug,user_id)


class UserRepository(object):
    def __init__(self, adapter=None):
        if not adapter:
            raise ValueError("Invalid repository implementation")
        self.client = adapter()

    def find(self, user_id):
        return self.client.find(user_id)

    def create(self, user_id):
        return self.client.create(user_id)

    def update(self, user):
        return self.client.update(user)

    def delete(self, user_id):
        return self.client.delete(user_id)

    def find_key(self,key):
        return  self.client.find_key(key)
