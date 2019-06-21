#!/usr/bin/env python
# coding:utf-8
from config import STATIC_PATH
from .base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        f = STATIC_PATH + "/index.html"
        with open(f, "r") as f:
            text = f.read()
        return text
