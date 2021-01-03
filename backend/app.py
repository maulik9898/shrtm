import json
import os

from bson import json_util
from flask import Flask, request, jsonify, Response
from flask_restful import Api
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix

from auth.middleware import firebase_initialization
from exceptions.invalidapiusage import InvalidAPIUsage
from database.mongo import initialize_db
from resources import initialize_routes

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
CORS(app)

api_app = Api(app)

initialize_routes(api_app)
firebase_initialization()

initialize_db(app)


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(e):
    return Response(json.dumps(e.to_dict(),default=json_util.default), mimetype="application/json", status=e.status_code)


@app.route("/", methods=["GET"])
def hello():
    """ Return a friendly HTTP greeting. """
    who = request.args.get("who", "World")
    return f"Hello {who}!\n"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
