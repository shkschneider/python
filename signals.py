#!/usr/bin/python -tt

import sys
import signal

def handler(signal, frame):
    print ''
    print 'Signal #%d received' % (signal)
    sys.exit(1)

signal.signal(signal.SIGINT, handler)
while True:
    continue
