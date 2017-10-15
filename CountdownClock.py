#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Timer done. Goodbye!\n\n')

countTime=int(input("How long do you want to count for (in seconds)?: "))
countdown(countTime)