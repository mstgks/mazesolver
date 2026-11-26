from tkinter import Tk, BOTH, Canvas
from graphics import Window, Point, Line
from cell import Cell



def main():
    win = Window(800, 600)

    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(128, 128, 256, 384)

    c2 = Cell(win)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c2.draw(384, 384, 480, 480)

    c1.draw_move(c2)

    c3 = Cell(win)
    c3.has_top_wall = False
    c3.has_right_wall = False
    c3.draw(512, 512, 640, 640)

    c2.draw_move(c3)

    win.wait_for_close()


main()