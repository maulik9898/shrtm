from flask import Flask, render_template, redirect
from flask_restful import Api
from flask_cors import CORS
from resources.root import api
from database.mongo import initialize_db
from resources import initialize_routes

app = Flask(__name__)
CORS(app)

api_app = Api(app)

initialize_routes(api_app)

initialize_db(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<slug>', methods=['GET'])
def redirects(slug):
    res , code = api.find_url(slug)
    return redirect(res['originalUrl'], 302)


if __name__ == '__main__':
    app.run()
