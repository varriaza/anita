from flask import Blueprint
api = Blueprint('api', __name__)
from . import connect, hd, slow, wv, adu5