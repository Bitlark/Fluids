from flask import jsonify
from app.apis.api import bp
from random import randint
from faker import Faker


@bp.route('/sample', methods=['GET', 'POST'])
def sample():
    fake = Faker('zh_CN')
    return jsonify({
        "msg": "sample>>> random:{},fakename={}".format(randint(0, 100000),fake.name())
    })
