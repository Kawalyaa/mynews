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

    def put(self, page_id):
        """Updating a single page in the news using id"""
        for apage in my_news:
            if apage['page_id'] == page_id:
                req = request.get_json()
                apage['tittle'] = req['tittle']
                apage['details'] = req['details']
                apage['updated'] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                return make_response(jsonify({
                    "message": "ok",
                    "apage": apage
                }), 200)
        req = request.get_json()
        creat_new = {
            "page_id": page_id,
            "tittle": req['tittle'],
            "details": req['details'],
            "updated": datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        }
        my_news.append(creat_new)
        return make_response(jsonify({
            "message": "ok",
            "apage": creat_new
        }), 201)
        
    def delete(self, page_id):
        """Deleting a single page in the news by id"""
        delete_news = [apage for apage in my_news if apage['page_id'] == page_id]

        """Checking wether the page_id input is empty or page_id provided does'nt exist"""
        if len(delete_news) == 0:

            return make_response(jsonify({
                "page_id": "Not found"
            }), 404)
        my_news.remove(delete_news[0])
        return make_response(jsonify({
            'message': 'news with page_id {} is deleted'.format(page_id)
        }), 200)
