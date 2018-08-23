from flask import Blueprint
from app.exts import CORS
from app.utils import import_all_submods

bp = Blueprint('index', __name__, url_prefix='')

CORS(bp)

import_all_submods(__name__)
