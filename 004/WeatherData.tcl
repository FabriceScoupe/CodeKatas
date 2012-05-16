#!/bin/sh
# \
exec tclsh "$0" "$@"

# Code Kata Four - Data Munging - Weather Data
# ============================================
# In weather.dat, find day with max temperature spread, ie
# max(max temperature - min temperature)

foreach {max_day max_mxt max_mnt max_spread} {0 0 0 0} break;

set fd [open "weather.dat" "r"]
while { [gets $fd line] >= 0 } {
    if { [regexp -- {^ *([0-9]+) +([0-9]+) +([0-9]+)} $line m dy mxt mnt] } {
        puts "Day: $dy MaxTemp: $mxt MinTemp: $mnt Spread: [expr $mxt - $mnt]"
        if { [expr $mxt - $mnt] > $max_spread } {
            set max_day $dy
            set max_mxt $mxt
            set max_mnt $mnt
            set max_spread [expr $mxt - $mnt]
        }
    }
}
close $fd

puts "Day with max temperature spread: $max_day, $max_mxt-$max_mnt=$max_spread"
