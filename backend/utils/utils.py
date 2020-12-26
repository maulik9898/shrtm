import secrets
import string


def generate_random_key(length):
    slug = ''.join(
        secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(length))
    return slug
