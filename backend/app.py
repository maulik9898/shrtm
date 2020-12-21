from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from database.mongo import initialize_db
from resources import initialize_routes

app = Flask(__name__)
CORS(app)

api = Api(app)

initialize_routes(api)

initialize_db(app)

if __name__ == '__main__':
    app.run()
