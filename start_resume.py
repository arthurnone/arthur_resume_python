#!/usr/bin/env python
# coding:utf-8
from app import app
from config import DEBUG, HOST, PORT, SCREAT_KEY

app.secret_key = SCREAT_KEY

app.run(
    debug=DEBUG,
    host=HOST,
    port=PORT
)
