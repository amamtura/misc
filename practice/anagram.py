#!/usr/bin/env python

import operator

u1 = u'jim \u00E9 morrison'
u2 = u'\u00E9 mr mojo risin'

print u1
print u2

l1 = [y.strip() for y in u1 if y.strip()]
l2 = [y.strip() for y in u2 if y.strip()]

l = l1 + l2

print l1
print l2

if reduce(operator.xor, [ord(x) for x in l]) == 0:
  print 'anagram'
else:
  print 'SORRY'
