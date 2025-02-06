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
