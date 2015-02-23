#!/usr/bin/env python

def flatten(root)
    if root == None:
        return
    
    s = [root]
    curr = None
    while len(s) > 0:
        n = s.pop()
        if n.right:
            s.append(n.right)
        if n.left:
            s.append(n.left)
        if curr:
            curr.right = n
            curr.left = None
        curr = n
