#!/bin/sh

pip --version
pip install git+https://github.com/jaraco/path.git --upgrade --force-reinstall -t local_lib --log ./history.log
