import os

from flask import Flask, render_template, redirect, request
from flask_restful import Api
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix

from auth.middleware import firebase_initialization
from resources.link import api
from database.mongo import initialize_db
from resources import initialize_routes

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
CORS(app)

api_app = Api(app)

initialize_routes(api_app)
firebase_initialization()

initialize_db(app)


@app.route("/", methods=["GET"])
def hello():
    """ Return a friendly HTTP greeting. """
    who = request.args.get("who", "World")
    return f"Hello {who}!\n"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
