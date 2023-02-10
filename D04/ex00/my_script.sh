#!/bin/sh

ENV_NAME=django_venv

python3 -m virtualenv -p python3 $ENV_NAME
. $ENV_NAME/bin/activate
pip install -r requirement.txt