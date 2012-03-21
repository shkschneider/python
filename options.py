#!/usr/bin/python -tt

'''
Need python-argparse module
'''

import sys
import argparse

parser = argparse.ArgumentParser(description='little description about this python script', prog='name', epilog='footer notes', add_help=True)
parser.add_argument('-o', '--output', dest='output', type=str, nargs=1, default='stdout', metavar='FILE', help='little help about -o')
parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False, help='little help about -v')
parser.add_argument('-i', '--input', dest='input', action='append', metavar='FILE', nargs=1, help='little help about -i')
parser.add_argument('-I', '--inputs', dest='inputs', type=str, metavar='FILE ...', nargs='+', default='stdin', help='little help about -I')
parser.add_argument('-p', '--port', dest='port', type=int, metavar='PORT', nargs=1, default='8080', help='little help about -p')
parser.add_argument('-P', '--ports', dest='ports', type=int, metavar='PORTS', nargs='+', default='8080', help='little help about -P')
parser.add_argument('-c', '--count', dest='count', action='count', help='little help about -c')
parser.add_argument('-V', '--version', action='version', version='%(prog)s 1.0')
parser.add_argument('str', nargs='*')
args = parser.parse_args()
print args
