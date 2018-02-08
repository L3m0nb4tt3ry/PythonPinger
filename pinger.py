#!/usr/bin/env python
import sys
import datetime
import os
def ping(address):
    if((os.system('ping %s -n 1' % (address,)))==0):
        with open('result.txt','a') as file:
            file.write("\nHost %s is up" %(address))
    else:
        with open('result.txt','a') as file:
            file.write("\nHost %s is down"%(address))

with open('result.txt','a') as res:
    res.write(str(datetime.datetime.now()))
with open("list.txt") as f:
    for line in f:
        ping(line)
