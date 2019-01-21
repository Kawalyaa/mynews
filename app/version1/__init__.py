"""We are now creating our flask instance or object called app from Flask class"""
from flask import Flask
from flask_restful import Resource
from flask_restful import Api
from app.version1.views import News
from app.version1.views import SinglePage


app = Flask(__name__)
api = Api(app)

"""Linking resources to the app"""

api.add_resource(News, '/news')
api.add_resource(SinglePage, '/mynews/<int:page_id>')

"""We are now importing our routes from views"""

from app.version1 import views
