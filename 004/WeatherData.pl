#!/usr/bin/perl
use strict;
use warnings;

# Code Kata Four - Data Munging - Weather Data
# ============================================
# In weather.dat, find day with max temperature spread, ie
# max(max temperature - min temperature)

my ($max_day, $max_mxt, $max_mnt, $max_spread) = (0, 0, 0, 0);

open(my $fd, "<", "weather.dat") || die $?;
while (<$fd>) {
    if (/^ *([0-9]+) +([0-9]+) +([0-9]+)/) {
        print "Day: $1 MaxTemp: $2 MinTemp: $3 Spread: ".($2-$3)."\n";
        if ($2-$3 > $max_spread) {
            ($max_day, $max_mxt, $max_mnt, $max_spread) =
                ($1, $2, $3, $2-$3);
        }
    }
}
close($fd);

print "Day with max temperature spread: $max_day, $max_mxt-$max_mnt=$max_spread\n";
