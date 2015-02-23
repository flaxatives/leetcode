#!/usr/bin/env python

"""
Given strings S and T, finds the minimum substring of S which contains all the
characters in T. Done in O(n) time.
"""
def min_window(S, T):
        freq = {}
        for letter in T:
            freq[letter] = 0

        # search S until we find a substring with all chars
        start = 0
        while start < len(S) and S[start] not in T:
            start += 1

        if start > len(S):
            return ""

        end = start
        allfound = False
        while not allfound and end < len(S):
            char = S[end]
            if char in T:
                freq[char] += 1
            allfound = allfound or all((freq[c] > 0 for c in T))
            end += 1
        end -= 1

        if end == len(S):
            return ""
        
        # search the rest of the string for smaller windows
        min_start = start
        min_end = end
        end += 1
        while end < len(S):
            # expand on the right side until we match the front char
            while end < len(S) and S[start] != S[end]:
                if S[end] in freq:
                    freq[S[end]] += 1
                end += 1
            if end >= len(S):
                break
            
            # remove excess characters from the front
            start += 1
            while start < end:
                char = S[start]
                if char in T and freq[char] > 1:
                    freq[S[start]] -= 1
                elif char in T and freq[char] == 1:
                    break
                start += 1
            
            # check if new window is smaller
            if end - start < min_end - min_start:
                min_start, min_end = start, end

            end += 1

        return S[min_start:min_end+1]

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 3:
        print(min_window(*sys.argv[1:3]))
