#! usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_graphql import GraphQLView

from flask_cors import CORS, cross_origin

from lagql_app.ext import db
from lagql_app.schema import schema


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('lagql_app.config')
    app.secret_key = app.config['SECRET_KEY']
    app.config['CORS_HEADERS'] = 'Content-Type'

    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True, context={'session': db.session}))
    app.url_map.strict_slashes = False

    db.init_app(app)

    @cross_origin(origin='localhost',headers=['ContentType','Authorization'])
    @app.route('/')
    def hello_world():
        return 'Go to /graphql'

    return app


app = create_app()


if __name__ == "__main__":
    app.run()
