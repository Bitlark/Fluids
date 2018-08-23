from flask import jsonify
from app.apis.api_v1 import bp
from random import randint
from faker import Faker


@bp.route('/user', methods=['GET', 'POST'])
def v1_user():
    fake = Faker('zh_CN')
    return jsonify({
        "msg": "sample>>> random:{},fakename={}".format(randint(0, 100000),fake.name())
    })
