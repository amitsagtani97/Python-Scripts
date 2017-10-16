#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)	# convert in to minutes and seconds for countdown
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Timer done. Goodbye!\n\n')

readTime=input("How long do you want to count for (mm:ss)?: ")
minutes, seconds = readTime.split(':')
countTime=int(minutes) * 60 + int(seconds)
countdown(countTime)
