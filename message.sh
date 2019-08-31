#!/bin/bash
if [ $# -ne 1 ]; then
  echo "usage: message.sh message" 1>&2
  exit 1
fi
./hub-ctrl -b 20 -d 6 -P 2 -p 1
sleep 2
sudo python3 ./message.py $1
sudo python3 ./led-badge-11x44.py message.png
sleep 1
./hub-ctrl -b 20 -d 6 -P 2 -p 0

