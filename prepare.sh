#!/bin/bash
virtualenv --no-site-packages --distribute venv && chmod u+x ./venv/bin/activate && source ./venv/bin/activate && pip install -r requirements.txt
