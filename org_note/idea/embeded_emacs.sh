#!/bin/bash

EMACS_CLIENT=/usr/bin/emacsclient
EMACS=/usr/bin/emacs
socket=$HOME/.emacs.d/server/server

if [ ! -e $socket ]; then
   $EMACS &
   while [ ! -e $socket ]; do
     sleep 1
   done
fi

$EMACS_CLIENT \
  --no-wait \
  --socket-name=$socket "$@"
