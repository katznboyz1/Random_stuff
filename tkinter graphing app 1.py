equation = str(input('Equation in [y = mx + b] format: '))

x = 0
y = None
lx = 0
ly = 0

from tkinter import *

base = Tk()
base.title(equation)
base.minsize(width = 1580, height = 800)
base.maxsize(width = 1580, height = 800)

canvas = Canvas(width = 1580, height = 800, bg = 'black', highlightthickness = 0)
canvas.place(x = 0, y = 0)

canvas.create_line(790, 0, 790, 800, fill = 'white')
canvas.create_line(0, 400, 1580, 400, fill = 'white')

for _ in range(-790, 790):
    x = _
    exec(equation)
    if x != -790: canvas.create_line((int(x + 790)), (int(y + 400)) - (y * 2), (int(lx + 790)), (int(ly + 400)) - (ly * 2), fill = 'green')
    lx = x
    ly = y

base.mainloop()
