#!/usr/bin/env python

import os
import sys
import commands

args = sys.argv[1:]
if not args:
    print 'Usage: %s <cmd ...>' % (sys.argv[0])
    sys.exit(1)

for cmd in args:
    # exact system call
    os.system(cmd)

for cmd in args:
    # line by line, with status
    (status, output) = commands.getstatusoutput(cmd)
    if status:
        print 'Error #%d' % (status)
        continue
    print output

# EOF
