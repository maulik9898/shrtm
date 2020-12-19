class Repository(object):
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

    def delete(self, slug):
        return self.client.delete(slug)
