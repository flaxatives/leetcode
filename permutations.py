#!/usr/bin/env python

def permute(nums):
    if len(nums) == 1:
        return [nums]

    l = []
    first = nums[0]
    rest = nums[1:]
    print(rest)
    permuted = permute(rest)
    for list in permuted:
        for i in range(len(list)+1):
            l.append(list[:i] + [first] + list[i:])

    return l

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(permute([int(x) for x in sys.argv[1:]]))

