import os
import sys

from flask import Flask
from flask_json import FlaskJSON, as_json
from . import db
from . import auth
from . import blog
from . import graph

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    FlaskJSON(app)
    try:
        env = os.environ['FLASK_ENV']
    except KeyError:
        env = 'development'
    try:
        app.config.from_object('config.{}Config'.format(env.capitalize()))
    except ImportError:
        pass
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        if not os._exists:
            os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    app.register_blueprint(auth.bp)
    # app.register_blueprint(blog.bp)
    app.register_blueprint(graph.bp)
    app.add_url_rule('/', endpoint='index')

    @app.route('/hello')
    @as_json
    def hello():
        return dict(name='Arun', age=31)
    return app

def checkForFile(path='C:/Users/arun.alex/Personal/Python/testcase_visualizer/flaskr/datas.csv'):
    csv_file = open(path, 'r')
    print('Enter')
    for line in csv_file:
        print(line)