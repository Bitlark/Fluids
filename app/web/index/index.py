from flask import current_app, render_template
from app.web.index import bp


@bp.route('/')
def index():
    rules_map = current_app.url_map._rules_by_endpoint
    return render_template('index.html', rules_map=rules_map)
