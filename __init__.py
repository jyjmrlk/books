#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "books"}
app.config["SECRET_KEY"] = "mysecretkey"

db = MongoEngine(app)

from books.views import book
app.register_blueprint(book.bp, url_prefix='/book')

login_manager = LoginManager()
login_manager.init_app(app)

if __name__ == '__main__':
    app.run()
