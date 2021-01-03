from flask import render_template, request, make_response
from flask_restful import Resource
from werkzeug.utils import redirect

from service.linkservice import LinkService

api = LinkService()


class Protected(Resource):

    def get(self, slug):
        error = ''
        error = request.args.get('error')
        print(error)
        r = make_response(render_template('password.html', error=error))
        r.headers.set('Content-Type', "text/html")
        return r

    def post(self, slug):
        res, code = api.find_url(slug)
        if code != 200:
            return f" url not found", code
        if res['password'] == request.form['password']:
            return redirect(res['originalUrl'], 302)
        return redirect('/' + slug + '/protected?error=Wrong password', 302)
