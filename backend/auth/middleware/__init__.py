import firebase_admin
from firebase_admin import credentials

def firebase_initialization():
    cred = credentials.Certificate('service.json')
    default_app = firebase_admin.initialize_app(credential=cred)
