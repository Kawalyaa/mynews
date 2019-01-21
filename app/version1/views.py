from flask_restful import Resource
from flask import request, abort, jsonify, make_response
import time
import datetime

from app.version1.models import my_news


class News(Resource):
    def post(self):
        """Creating a new article"""
        req = request.get_json()
        new = {
            "news_id": len(my_news) + 1,
            "tittle": req['tittle'],
            "description": req['description'],
            "date": datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        }
        my_news.append(new)
        return make_response(jsonify({
            "msg": "Created",
            "news_id": new['news_id']
        }), 201)

    def get(Resouce):
        """retrieving all news"""
        pass


class SingleArticleNews(Resource):
    """class for single news"""
    def get(self, id):
        """Rettrieving a sing article in the news by id"""
        pass

    def put(self, id):
        """Updating a single article in the news using id"""
        pass

    def deleting(self, id):
        """Deleting a single article in the news by id"""
        pass
