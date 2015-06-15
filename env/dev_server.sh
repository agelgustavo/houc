#!/usr/bin/env bash

if [ ! -d "../lib" ]; then
    ln -s ~/.virtualenvs/houc/lib/python2.7/site-packages/ lib
fi

/usr/local/google_appengine/dev_appserver.py $1
