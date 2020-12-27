from flask import Flask, render_template, redirect
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


@app.route('/<slug>', methods=['GET'])
def redirects(slug):
    res, code = api.find_url(slug)
    return redirect(res['originalUrl'], 302)


if __name__ == '__main__':
    app.run()
