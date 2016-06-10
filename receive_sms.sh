#!/bin/sh
from=$SMS_1_NUMBER
message=$SMS_1_TEXT

echo "Received SMS: $message" >> inbox.log
echo "Hello world!" | sudo gammu sendsms TEXT "$from"
