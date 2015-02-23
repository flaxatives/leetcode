#!/usr/bin/env python

solved = {}
def numDecodings(s):
    if s == "" or s.startswith("0"):
        return 0

    if len(s) == 1:
        if int(s) == 0:
            return 0
        else:
            return 1
    
    if len(s) == 2:
        if int(s) <= 26:
            return numDecodings(s[1]) + numDecodings(s[0])
        else:
            return numDecodings(s[1])
    
    if s in solved:
        return solved[s]
        
    n = 0
    left, right = s[:-1], s[-1:]
    if ischar(right) and numDecodings(left) != 0:
        n += numDecodings(left)
    left, right = s[:-2], s[-2:]
    if ischar(right) and numDecodings(left) != 0:
        n += numDecodings(left)

    solved[s] = n
    return n

def ischar(s):
    if s == "" or s.startswith("0"):
        return 0
    elif len(s) == 1:
        return int(s) != 0
    elif len(s) == 2:
        return 1 <= int(s) <= 26
    return False

if __name__ == "__main__":
    import sys
    for i in sys.argv[1:]:
        print "{0}: {1}".format(i, numDecodings(i))
