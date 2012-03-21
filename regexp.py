#!/usr/bin/python -tt

import re

print re.match(r'www', 'http://twitter.com/leonnib4')
print re.match(r'http', 'http://twitter.com/leonnib4')
match = re.search(r'^([a-z]+)://', 'http://shkschneider.me')
if match:
    print match.group()
else:
    print 'Not Found'
print re.split('[a-fA-Z]+', '0a3B9')
print re.sub(r'\sand\s', ' & ', 'Baked Beans and Spam')
print re.findall(r'^([a-z]+)://(\w+)\.?', 'http://www.shkschneider.me/uri', flags=re.IGNORECASE)
print re.findall(r'[a-z]+', 'a0b1c2d3e4f5', flags=re.IGNORECASE)

input = '''Ross McFluff: 834.345.1254 155 Elm Street

Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way


Heather Albrecht: 548.326.4584 919 Park Place'''
entries = re.split('\n+', input)
for entry in entries:
    print re.findall(r'^([^:]+): ([0-9\.]+) (.+)$', entry.strip(), flags=re.IGNORECASE)
