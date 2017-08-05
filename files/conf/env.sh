#! /bin/sh

# activate virtualenv if present
if [ -e venv ]
then
    echo "Activating virtualenv"
    . venv/bin/activate
fi

# import configuration if present
if [ -e vars.sh ]
then
    echo "Exporting vars.ini"
    . vars.sh
fi
