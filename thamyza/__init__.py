from flask import Flask, request

app = Flask(__name__)

from thamyza.controllers import index