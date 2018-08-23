#!/usr/bin/env bash

source ./LANG.sh

#******** set Flask ENV

export FLASK_APP=app
export FLASK_ENV=testing


flask run --host=0.0.0.0 --port=5000