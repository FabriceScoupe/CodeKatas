#!/usr/bin/python

# Code Kata Four - Data Munging - DRY Fusion
# ==========================================
# DRYFusion module provides common functionality.

import re

# ========== SHARED FUNCTIONALITY ==========
# Generator returning groups in each matched line
# Can work on big files.
def next_line(filename, compiled_pattern):
    for line in iter(open(filename).readline, ''):
        m = compiled_pattern.match(line)
        if m: yield m.groups()

# General search in file 
def search(filename, pattern, tuple_reduce, row_reduce, printformat):
    cp = re.compile(pattern)
    found_g = []
    for g in next_line(filename, cp):
        found_g = [row_reduce(found_g+[g],key=tuple_reduce)]
        print printformat % (g+(tuple_reduce(g),))
    return found_g[0]
