from flask import Module

auth = Module(__name__)

@auth.route('/signup')
def signup():
    return """
           This page is signup<br />
           auth.py<br />
           url = '/signup'
           """

@auth.route('/login')
def login():
    return """
           This page is login<br />
           auth.py<br />
           url = '/login'
           """

@auth.route('/logout')
def logout():
    return """
           This page is logout<br />
           auth.py<br />
           url = '/logout'
           """
