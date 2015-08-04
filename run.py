#!/usr/bin/env python

import controller as c
import sys

x=c.controller(0.15,float(sys.argv[2])/100)
x.write_sequence(sys.argv[1])
x.play()
print sys.argv[1]
print sys.argv[2]
