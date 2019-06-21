#!/usr/bin/env python
# coding:utf-8
import os

# BASE CONFIG
DEBUG = False
HOST = "0.0.0.0"
PORT = 20193

SCREAT_KEY = ""

# path
PATH = os.path.abspath(os.path.dirname(__file__))
WWW_PATH = os.path.abspath(os.path.dirname(PATH))

REACT_PATH = os.path.abspath(os.path.join(WWW_PATH, "arthur-resume-react"))
STATIC_PATH = os.path.abspath(os.path.join(REACT_PATH, "dist"))

try:
    from local_config import *
except Exception as e:
    print(e)
