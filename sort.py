#!/usr/bin/python -tt

# lists
print sorted([4, 2, 1, 6])

# tuples
l = [(1, 'b'), (2, 'a'), (1, 'c')]
print sorted(l)

# custom
print sorted(['b', 'cc', 'aaa'], key=len, reverse=True)

# ...
