#!/usr/bin/python -tt

import sys

argc = len(sys.argv)
argv = sys.argv
print '%d: %s' % (argc, argv)

for i in range(1, len(sys.argv)):
    print '#' + str(i) + ':', sys.argv[i]

for s in sys.argv[1:]:
    print s

del sys.argv[0]
print sys.argv
