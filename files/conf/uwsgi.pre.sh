#! /bin/sh

# should run ASAP to create needed directories and links

DIR=$(cd $(dirname "$0"); pwd)

# check if run directory exists, create if not
test -e $DIR/run || mkdir -p $DIR/run

# correct owner and permissions
chown www-data:www-data $DIR/run
chmod 770 $DIR/run

# check if socket file exists and it is not a link
test -e $DIR/uwsgi.sock && (test -L $DIR/uwsgi.sock || rm -f $DIR/uwsgi.sock)

# check if socket link exists, create if not
test -L $DIR/uwsgi.sock || ln -sr $DIR/run/uwsgi.sock $DIR/uwsgi.sock
