from flask import Blueprint
from app.exts import CORS
from app.utils import import_all_submods

bp = Blueprint('api_v1', __name__, url_prefix='/api/v1')

CORS(bp)

import_all_submods(__name__)
