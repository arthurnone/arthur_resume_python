#!/usr/bin/env python
# coding:utf-8
import json
from flask.views import MethodView
from flask import make_response

from config import DEBUG


class BaseHandler(MethodView):
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__()

    def json_response(self, status, msg='', data={}, **kwargs):
        data = {
            'status': status,
            'msg': msg,
            'data': data
        }
        data.update(kwargs)
        data = json.dumps(data)
        resp = make_response(data)
        resp.headers['Content-Type'] = 'application/json'
        return resp

