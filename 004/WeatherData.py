#!/usr/bin/python

# Code Kata Four - Data Munging - Weather Data
# ============================================
# In weather.dat, find day with max temperature spread, ie
# max(max temperature - min temperature)

import re

pattern = re.compile('^ *([0-9]+) +([0-9]+) +([0-9]+)')

# Extract lines from weather.dat matching pattern, store matched groups
# This swallows the whole file, so not suitable for big files.
# groups = list of tuples: (day, max temp., min temp.)
groups = [tuple([int(x) for x in pattern.match(line).groups()])
             for line in open("weather.dat").readlines()
                 if pattern.match(line)]

# Define spread as lambda function on (day, max temp., min temp.) tuples.
# Returns a singleton (for printing purposes).
spread = lambda(x, y, z) : (y-z,)

print "\n".join(["Day: %d MaxTemp: %d MinTemp: %d Spread %d" % (g+spread(g))
                    for g in groups])

# Find tuple in groups with max temperature spread, using spread function
g = max(groups, key = spread);

print "Day with max temperature spread: %d, %d-%d=%d" % (g+spread(g))
