#!/usr/bin/env python

import captain

import controller as c

def main(notes):
    x=c.controller(.1,.05)
    x.write_sequence(notes)
    x.play()
    print "chile"
    return 0
