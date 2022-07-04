#!/bin/sh

if [ $XDG_SESSION_TYPE == 'wayland' ] || [ $XDG_SESSION_TYPE == 'x11' ]
then
	python3 gui/main.py
elif [ $XDG_SESSION_TYPE == 'tty' ]
then
	python3 cli/main.py
else
	echo "Unknown sesion type"
fi

