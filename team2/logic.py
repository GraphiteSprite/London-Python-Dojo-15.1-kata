#!/usr/bin/env python

from time import sleep

import board


position = {"x": 50, "y": 50}

# 0 -> up, 1 -> right, 2 -> down, 3 -> left
direction = 0

size = 100


def play():
    grid = board.Board((size, size))

    for i in range(10000):
        turn(grid)
        grid.draw()
        print()
        # sleep(0.2)




def turn(grid):
    global direction
    colour = grid[position["x"], position["y"]]

    match colour:
        case board.Empty | 0:
            direction = (direction + 1) % 4
            grid[position["x"], position["y"]] = 1
            move()
        case 1:
            direction = (direction + 3) % 4
            grid[position["x"], position["y"]] = 0
            move()


def move():
    match direction:
        case 0:
            position["y"] = (position["y"] + size - 1) % size
        case 1:
            position["x"] = (position["x"] + 1) % size
        case 2:
            position["y"] = (position["y"] + 1) % size
        case 3:
            position["x"] = (position["x"] + size - 1) % size


if __name__ == "__main__":
    play()
