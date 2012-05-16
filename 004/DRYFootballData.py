#!/usr/bin/python

# Code Kata Four - Data Munging - DRY Fusion
# ==========================================
# Football Data using DRYFusion for common functionality.

import DRYFusion

f = lambda (n, gf, ga) : abs(int(gf)-int(ga))
x = DRYFusion.search("football.dat",
        '^ *[0-9]+\. +([A-Za-z_]+) +'+('[^ ]+ +'*4)+'([0-9]+) +- +([0-9]+)',
        f, min, "%20s: |%s for - %s against| = %s")

print "\nTeam with min goal difference: %s, |%s-%s|=%d" % (x+(f(x),))
