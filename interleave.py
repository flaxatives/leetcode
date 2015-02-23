#!/usr/bin/env python

def interleave_naive(a,b,c):
    if len(a) + len(b) != len(c):
        return False

    i = j = k = 0
    while i < len(a) or j < len(b):
        print("Comparing {0} {1} {2}".format(a[i:],b[j:],c[k:]))
        if i < len(a) and a[i] == c[k]:
            i += 1
            k += 1
        elif j < len(b) and b[j] == c[k]:
            j += 1
            k += 1
        else:
            return False
    return True

def interleave(a,b,c):
    if len(a) + len(b) != len(c):
        return False
    if a == b == c == "":
        return True

    if len(c) == 1:
        return a == c or b == c

    aworks = bworks = False
    if len(a) > 0 and a[0] == c[0]:
        aworks = interleave(a[1:],b,c[1:]) 
    if len(b) > 0 and b[0] == c[0]:
        bworks = interleave(a,b[1:],c[1:]) 
    return aworks or bworks

    return interleave(a[1:],b,c[1:]) or interleave(a, b[1:], c[1:])
    

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 4:
        a,b,c = sys.argv[1:]
        answer = interleave_naive(a,b,c)
        print("{0} + {1} = {2}: {3}".format(a,b,c,answer))
