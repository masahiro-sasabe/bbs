from flask import Module

home = Module(__name__)

@home.route('/')
def index():
    return """
           Hello World!<br />
           hello.py<br />
           url = '/'
           """
