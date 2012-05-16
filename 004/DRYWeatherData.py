#!/usr/bin/python

# Code Kata Four - Data Munging - DRY Fusion
# ==========================================
# Weather Data, using DRYFusion common functionality

import DRYFusion

f = lambda(dy, mxt, mnt) : int(mxt) - int(mnt)
x = DRYFusion.search("weather.dat", '^ *([0-9]+)\*? +([0-9]+) +([0-9]+)',
        f, max, "Day: %s MaxTemp: %s MinTemp: %s Spread %s")

print "\nDay with max temperature spread: %s, %s-%s=%d" % (x+(f(x),))
