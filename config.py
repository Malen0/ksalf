import os

class cofig(object):
    SECRET_KEY = os.environ.get("SECRET-KEY") or "you-will-never-gess"
    
