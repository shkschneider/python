#!/usr/bin/env python

'''
Need argparse module
'''

import argparse
import sys
import os

# action: store store_const store_true strore_false append append_const count help version
# nargs: N ? * +

parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]),
                                 description='little description about this python script',
                                 epilog='footer notes',
                                 add_help=True)
parser.add_argument('-o', '--output',  dest='output',  type=str,        metavar='FILE',     nargs=1,   default='stdout',  help='little help about -o')
parser.add_argument('-v', '--verbose', dest='verbose', action='store_true',                            default=False,     help='little help about -v')
parser.add_argument('-i', '--input',   dest='input',   action='append', metavar='FILE',     nargs=1,                      help='little help about -i')
parser.add_argument('-I', '--inputs',  dest='inputs',  type=str,        metavar='FILE ...', nargs='+', default='stdin',   help='little help about -I')
parser.add_argument('-p', '--port',    dest='port',    type=int,        metavar='PORT',     nargs=1,   default=80,        help='little help about -p')
parser.add_argument('-P', '--ports',   dest='ports',   type=int,        metavar='PORTS',    nargs='+', default=[80, 443], help='little help about -P')
parser.add_argument('-c', '--count',   dest='count',   action='count',                                                    help='little help about -c')
parser.add_argument('-V', '--version',                 action='version', version='%(prog)s 1.0')
parser.add_argument(                   'argv',                                              nargs='*',                    help='little help about argv')
args = parser.parse_args()

print 'output:', args.output
print 'verbose:', args.verbose
print 'input:', args.input
print 'inputs:', args.inputs
print 'port:', args.port
print 'ports:', args.ports
print 'count:', args.count
print 'argv:', args.argv

#parser.parse_args(['--version'])

#parser.print_help()

# EOF
