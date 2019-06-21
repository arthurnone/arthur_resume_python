#!/usr/bin/env python
# coding:utf-8
from .base import BaseHandler
from flask import request
from .resume_query import ResumeSchema


class ResumeHandler(BaseHandler):
    def graphql(self, q):
        data = ResumeSchema.execute(q)
        return data.data

    def get(self, *args, **kwargs):
        q = request.args.get('q')
        data = self.graphql(q)

        return self.json_response(status=1, data=data)
