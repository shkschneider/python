#!/usr/bin/env python

import sys

args = sys.argv[1:]
if not args:
    print 'Usage: %s <file ...>' % (sys.argv[0])
    sys.exit(1)
for filename in args:
    try:
        f = open(filename)
    except IOError:
        print 'IOError intercepted'
        #raise IOError

#EOF
