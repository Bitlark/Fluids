from flask import Blueprint
from app.exts import CORS
from app.utils import import_all_submods

bp = Blueprint('api', __name__, url_prefix='/api')

CORS(bp)

import_all_submods(__name__)
