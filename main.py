# coding=utf-8
"""
@author: Hanson
@software: Pycharm2022
@file: main_swagger_ui.py
@time: 2023-03-28 14:05:11
@desc: 
"""

from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api_app = Api(app=app,
              version='1.0',
              title='Main',
              description='Main APIs')
name_space = api_app.namespace(name='helloworld',
                               description='The helloworld APIs EndPoint.')


@name_space.route('/')
class HelloWorld(Resource):
    @staticmethod
    def get(self):
        return {
            'status': 'you get a request.'
        }

    @staticmethod
    def post(self):
        return {
            'status': 'you post a request.'
        }


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
    # gunicorn -c gunicorn.conf main:app
