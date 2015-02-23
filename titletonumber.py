#!/usr/bin/env python

def titleToNumber(s):
    if len(s) == 0:
        return None

    if len(s) == 1:
        return ord(s) - ord("A") + 1

    prefix = s[:-1]
    lastletter = s[-1]
    return titleToNumber(prefix) * 26 + titleToNumber(lastletter)

if __name__ == "__main__":
    import sys, string
    for s in sys.argv[1:]:
        print("{0}: {1}".format(s, titleToNumber(s)))
