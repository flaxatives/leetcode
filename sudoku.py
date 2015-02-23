#!/usr/bin/env python

import random

BLANK = 0

# @param board, a 9x9 2D array
# Solve the Sudoku by modifying the input board in-place.
# Do not return any value.
def solve_bogo(puzzle):
    clone = []
    for i in range(len(puzzle)):
        clone.append([None] * len(puzzle))
    copy_from(puzzle, clone)

    # solve each block until valid
    while not valid(clone):
        copy_from(puzzle, clone)
        for i in range(0, len(clone), 3):
            for j in range(0, len(clone[i]), 3):
                solve_block(clone, i, j)

    copy_from(clone, puzzle)

""" Brute force solution via backtracking """
def solve_brute(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == BLANK:
                unused = set(range(1,10))
                row = puzzle[i]
                column = (r[j] for r in puzzle)
                
                # find which block it's a part of
                x = i - (i % 3)
                y = j - (j % 3)
                block = nums_in_block(puzzle, x, y)

                unused -= set(row)
                unused -= set(column)
                unused -= set(block)
                for n in unused:
                    puzzle[i][j] = n
                    if solve_brute(puzzle):
                        return True

                puzzle[i][j] = BLANK
                return False

    return valid(puzzle)

def copy_from(src, dest):
    for i in range(len(src)):
        for j in range(len(src[i])):
            dest[i][j] = src[i][j]

""" Solve the block at x, y """
def solve_block(puzzle, x, y):
    # find numbers not filled in yet
    available = list(range(1,10))
    for i in range(x, x+3):
        for j in range(y, y+3):
            num = puzzle[i][j]
            if num in available:
                available.remove(num)
    
    # fill them in
    for i in range(x, x+3):
        for j in range(y, y+3):
            num = puzzle[i][j]
            if num == BLANK:
                r = random.randint(0, len(available)-1)
                puzzle[i][j] = available.pop(r)

def valid(puzzle):
    for row in puzzle:
        if not valid_row(row):
            return False
    for column in zip(*puzzle):
        if not valid_row(column):
            return False
    
    # check valid blocks
    #for x in range (0, 10, 3):
    #    for y in range (0, 10, 3):
    #        if not valid_block(puzzle, x, y):
    #            return False

    return True

def valid_block(puzzle, x, y):
    nums = set(range(1,10))
    for i in range(x, x+3):
        for j in range(y, y+3):
            num = puzzle[x][y]
            nums.discard(num)
    return len(nums) == 0


def valid_row(row):
    return set(row) == set(range(1, 10))

def print_block(puzzle, x, y):
    for i in range(x, x+3):
        print(puzzle[i][y:y+3])
    print()

def print_puzzle(p):
    print("Puzzle")
    for i, row in enumerate(p):
        print("{0}    {1}    {2}".format(row[0:3], row[3:6], row[6:9]))
        if (i+1) % 3 == 0:
            print()

def nums_in_block(p, x, y):
    nums = []
    for i in range(x, x+3):
        for j in range(y, y+3):
            num = p[i][j]
            if num != BLANK:
                nums.append(num)
    return nums
