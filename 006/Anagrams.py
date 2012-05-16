#!/usr/bin/python

# Code Kata 6: Anagrams
# =====================

signature = lambda w : "".join(sorted(w))

# words with the same "signature" are anagrams.
def are_anagrams(words):
    s = ""
    for w in words:
        sw = signature(w)
        if ((s != "") and (sw != s)): return False
        s = sw
    return True

# Returns map: signature -> [words with that signature]
# without singletons (so only anagrams).
def anagrams(words):
    a = {}
    for w in words:
        s = signature(w)
        a[s] = (s in a) and a[s]+[w] or [w]
    return dict([(s,a[s]) for s in a if (len(a[s]) > 1)])

# List for Unit Tests
good_anagrams = [
    ["kinship", "pinkish"],
    ["enlist", "inlets", "listen", "silent"],
    ["boaster", "boaters", "borates"],
    ["fresher", "refresh"],
    ["sinks", "skins"],
    ["knits", "stink"],
    ["rots", "sort"],
    ["parsley", "players", "replays", "sparely"],
    ["arrest", "rarest", "raster", "raters", "starer", "sartre"],
    ["crepitant", "pittancer"],
    ["actaeonidae", "donatiaceae"],
    ["electoral", "recollate"]]

bad_anagrams = [
    ["humans", "humane"],
    ["nested", "dented"],
    ["sinks", "skins", "kings"],
    ["sort", "rots", "sorts"]]

print "Good anagrams:"
print "\n".join(["%s are%sanagrams." % \
                    (", ".join(l), are_anagrams(l) and " " or " NOT ")
                    for l in good_anagrams])

print "\nBad anagrams:"
print "\n".join(["%s are%sanagrams." % \
                    (",".join(l), (are_anagrams(l) and " " or " NOT ")) 
                    for l in bad_anagrams])

print "\nAnagrams in file wordlist.txt, sorted by length of sets and words:"
word_list = [l.rstrip('\n').lower() for l in open("wordlist.txt").readlines()]
anags = anagrams(word_list)

# for each list of words (values of anags), sort on tuple:
# (length of list, length of first word, first word itself)
# The default comparator works fine on those tuples.
# Join each sorted list with commas, then join the whole with new lines.
print "\n".join([", ".join(v) \
    for v in sorted(anags.values(), key=lambda l:(len(l),len(l[0]),l[0]))])

print "\nTotal number of anagrams: %d" % \
     reduce(lambda x,y: x+y, [len(v) for v in anags.values()])
print "Number of sets: %d" % len(anags.keys())
print "Longest words that are anagrams: %s" % \
    ", ".join(anags[max(anags.keys(), key=len)])
print "Set of anagrams with most words: %s" % \
    ", ".join(max(anags.values(), key=len))
