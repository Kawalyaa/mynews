from flask_restful import Resource
from flask import request, abort, jsonify, make_response
import time
import datetime

from app.version1.models import my_news


class News(Resource):
    def post(self):
        """Creating a new page"""
        req = request.get_json()
        new = {
            "page_id": len(my_news) + 1,
            "tittle": req['tittle'],
            "details": req['details'],
            "date": datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        }
        my_news.append(new)
        return make_response(jsonify({
            "msg": "Created",
            "page_id": new['page_id'],
            "date_created": new['date']
        }), 201)

    def get(Resouce):
        """retrieving all news"""
        return make_response(jsonify({
            "message": "ok",
            "news": my_news
        }), 200)


class SinglePage(Resource):
    """class for single page in news"""
    def get(self, page_id):
        """Rettrieving a sing article in the news by id"""
        for apage in my_news:
            if apage['page_id'] == page_id:
                return make_response(jsonify({
                    "message": "ok",
                    "news_page": apage,
                }), 200)
        return make_response(jsonify({
            "message": "Not found"
        }), 404)

    def put(self, my_id):
        """Updating a single page in the news using id"""
        pass

    def deleting(self, my_id):
        """Deleting a single page in the news by id"""
        pass
