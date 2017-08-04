#! /bin/sh

# activate virtualenv if present
test -e venv && . venv/bin/activate
# import configuration if present
test -e vars.sh && . vars.sh
