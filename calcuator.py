from tkinter import *
import math, random
from math import *

base = Tk()
base.title('Graphing calculator')
base.minsize(width = 300, height = 600)
base.maxsize(width = 300, height = 600)

frame = Frame(base, highlightthickness = 0, width = 300, height = 600, bg = 'gray')
frame.place(x = 0, y = 0)

class calculator():
    line1 = 'l1'
    line2 = 'l2'
    line3 = 'l3'
    operation = '+'
    others = {'MODE':'standard', 'FLOAT':8}
    def solve():
        pass
    def main():
        global frame
        frame.destroy()
        frame = Frame(base, highlightthickness = 0, width = 300, height = 600, bg = 'gray')
        frame.place(x = 0, y = 0)
        Canvas(frame, width = 290, height = 170, bg = 'black', highlightthickness = 0).place(x = 5, y = 5)
        Label(frame, font = 'Calibri 10', text = calculator.line1, bg = 'black', fg = 'white').place(x = 10, y = 60)
        Label(frame, font = 'Calibri 10', text = calculator.line2, bg = 'black', fg = 'white').place(x = 10, y = 80)
        Label(frame, font = 'Calibri 10', text = calculator.line3, bg = 'black', fg = 'white').place(x = 10, y = 100)
        Label(frame, font = 'Calibri 10', text = calculator.operation, width = 1, bg = 'black', fg = 'white').place(x = 270, y = 80)
        Label(frame, font = 'Calibri 10', text = calculator.others, bg = 'black', fg = 'white').place(x = 10, y = 10)
        

calculator.main()
#base.mainloop()
