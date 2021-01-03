import firebase_admin
from firebase_admin import credentials


def firebase_initialization():
    default_app = firebase_admin.initialize_app()
