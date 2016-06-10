#!/bin/bash

retval="ACK"
if [ "$1" = "uptime" ]; then
	retval="$(uptime | awk '{print $3}' | sed -e 's/,//')"
fi
if [ "$1" = "ip" ]; then
	retval="$(./get_public_ip.sh)"
fi

echo $retval
