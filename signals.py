#!/usr/bin/env python

import sys
import signal

def handler(sig, frame):
    print
    print 'Signal #%d received' % (sig)
    sys.exit(1)

signal.signal(signal.SIGINT, handler)
while True:
    continue

# EOF
