### What is Langton's Ant?

**Langton's Ant** simulates and visualizes the behavior of Langton's Ant, a well-known algorithmic automaton that moves on a grid and follows simple rules to create intricate patterns.

- **`logic.py`** contains the main logic for controlling Langton's Ant. It handles the movement and direction of the ant on a grid, as well as updating the grid's cells based on the ant's current position. The ant changes its direction and the state of the cell it occupies, creating a trail as it moves.
  
- **`display.py`** is responsible for the graphical user interface (GUI) that visualizes the grid and the ant's movement. It uses `graphics.py` to create a window and represent the grid as cells. It also allows users to manually interact with the grid by clicking cells to change their state and disrupt the ant's path.

### Workflow:
1. The project displays the ant's movement on a 100x100 grid, where each cell can be either white (empty) or black (occupied).
2. The ant starts at the center of the grid and follows these rules:
   - If the ant is on a white cell, it turns 90° clockwise, changes the cell to black, and moves forward.
   - If the ant is on a black cell, it turns 90° counterclockwise, changes the cell to white, and moves forward.
3. The user can click on cells to manually change their state, affecting the ant's movement.

### To Run:
1. Install the required dependencies:
   ```shell
   pip install board graphics.py
   ```
2. Run the `display.py` script to visualize Langton's Ant in action:
   ```shell
   python display.py
   ``` 



<!--
 // Prompt used to create these docs:



Please give a short description of what is happening in the following project: Title: Langton's Ant. Tree: ├── display.py
├── logic.py
└── README.md . Files: README.md 
## Langton's ant - team 2
shell
pip install board graphics.py
python display.py
Click on cells to switch their state manually and disrupt the ant.
 logic.py 
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
  logic.py 
import time

from board import Board, Empty
from graphics import GraphWin, Rectangle, Point

from logic import turn

CELLS_H = 100
CELLS_V = 100

cell_size_x = 1000 / CELLS_H
cell_size_y = 1000 / CELLS_V

b = Board((CELLS_H, CELLS_V))

gw = GraphWin("Langton's ant", 1000, 1000, autoflush=False)

gboard = {}

for i, j in b:
    r = Rectangle(
        Point(i * cell_size_y, j * cell_size_x),
        Point((i + 1) * cell_size_y, (j + 1) * cell_size_x)
    )
    r.draw(gw)
    gboard[i, j] = r


def update_cells():
    for i, j in b:
        r = gboard[i, j]
        r.setFill('black' if b[i, j] else 'white')
    gw.flush()

update_cells()

i = 0
while True:
    #time.sleep(0.0)
    turn(b)

    click = gw.checkMouse()
    if click:
        x = int(click.x / cell_size_x)
        y = int(click.y / cell_size_y)
        print(f"Clicked in cell ({x}, {y})")
        new = 0 if b[x, y] else 1
        b[x, y] = new

    if i % 10 == 0:
        update_cells()
    i += 1


gw.close() 
-->

