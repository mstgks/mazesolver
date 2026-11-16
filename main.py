from tkinter import Tk, BOTH, Canvas
from graphics import Window, Point, Line
from cell import Cell



def main():
    win = Window(800, 600)

    c = Cell(win)
    c.draw(128, 64, 256, 128)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(384, 384, 512, 512)

    win.wait_for_close()


main()