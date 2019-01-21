"""We are now creating our flask instance or object called app from Flask class"""
from flask import Flask
app = Flask(__name__)

"""We are now importing our routes from views"""
from version1 import views
