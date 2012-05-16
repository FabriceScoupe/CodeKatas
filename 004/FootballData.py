#!/usr/bin/python

# Code Kata Four - Data Munging - Football Data
# =============================================
# In football.dat, find name of team with the smallest difference
# between for and against goals.

import re
pattern = re.compile(
#       Id          Name           P, W, L, D    For          Against
    '^ *[0-9]+\. +([A-Za-z_]+) +'+('[^ ]+ +'*4)+'([0-9]+) +- +([0-9]+)')

# Generator returning groups in each matched line
# Can work on big files.
def next_line(filename, compiled_pattern):
    for line in iter(open(filename).readline, ''):
        m = compiled_pattern.match(line)
        if m: yield m.groups()

# Define goal difference as lambda function on (Name, For, Against) tuples.
# Returns a singleton (for printing purposes).
goaldiff = lambda (n, f, a) : (abs(int(f)-int(a)),)

# groups = list of tuples (name, # goals for, # goals against)
# groups is an iterable (generator) here.
min_g = (None, 0, 0)
for g in next_line("football.dat", pattern):
    min_g = min_g[0] and min(g, min_g, key=goaldiff) or g # x ? y : z in Python.
    print "%20s: |%s for - %s against| = %d" % (g+goaldiff(g))

print
print "Team with min goal difference: %s, |%s-%s|=%d" % (min_g+goaldiff(min_g))
