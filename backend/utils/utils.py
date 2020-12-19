import secrets
import string


def generate_slug():
    slug = ''.join(
        secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(7))
    return slug
