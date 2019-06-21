#!/usr/bin/env python
# coding:utf-8
from flask import Flask, send_from_directory, make_response

from config import STATIC_PATH
from handlers.index import IndexHandler
from handlers.resume import ResumeHandler

app = Flask(
    __name__,
    static_url_path="/static",
    static_folder=STATIC_PATH,
    template_folder=STATIC_PATH
)


@app.route('/app/<path:path>')
def app_handler(path):
    return send_from_directory(STATIC_PATH, path)


@app.route('/manifest.json')
def manifest():
    try:
        f = STATIC_PATH + "/manifest.json"
        with open(f, "r") as f:
            text = f.read()
        resp = make_response(text)
        resp.headers['Content-Type'] = 'application/json'
        return resp
    except Exception as e:
        return "404 not found", 404


app.add_url_rule('/', view_func=IndexHandler.as_view('index'))
app.add_url_rule('/cn', view_func=IndexHandler.as_view('index-cn'))
app.add_url_rule('/en', view_func=IndexHandler.as_view('index-en'))
app.add_url_rule('/nld', view_func=IndexHandler.as_view('index-nld'))
app.add_url_rule('/api/resume', view_func=ResumeHandler.as_view('api-resume'))
