#!/usr/bin/env bash

source ./LANG.sh

#export FLASK_APP="app:create_app('development')"
export FLASK_APP=app
export FLASK_ENV=development

flask run --host=0.0.0.0 --port=5000
