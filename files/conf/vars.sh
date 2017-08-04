#! /bin/sh
#
# how can I turn config ini file into system environment in bash?
#
# credits: http://stackoverflow.com/a/22535251/593907
#
set -a               # turn on automatic export
# source vars.ini      # execute all commands in the file
# skip .ini section header
cat vars.ini | grep -v "^\[.*\]$" | source /dev/stdin
set +a               # turn off automatic export
