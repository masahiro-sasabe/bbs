from flask import Flask
from apps.views.home import home
from apps.views.auth import auth

app = Flask(__name__)
app.register_module(home)
app.register_module(auth)
