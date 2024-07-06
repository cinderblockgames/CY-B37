#!/bin/bash
/home/droid/cy-b37/main.py 2>&1 | tee >(ts "[%H:%M:%S]" > /home/droid/logs/main_$(date +%Y-%m-%dT%H-%M-%S).log) &
/home/droid/cy-b37/ble.py 2>&1 | tee >(ts "[%H:%M:%S]" > /home/droid/logs/ble_$(date +%Y-%m-%dT%H-%M-%S).log) &
