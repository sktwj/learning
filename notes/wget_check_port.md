#!/bin/bash

wget --delete-after -t1 -T1 "http://$1:$2" 2>&1 | grep "connected" && echo ok || echo nok