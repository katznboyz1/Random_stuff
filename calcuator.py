#GRAPHING CALCULATOR SCRIPT COPYLEFT HARRISON LINDGREN <harrison.lindgren@gmail.com>

#DOES NOT WRITE LINEAR TO GRID YET

from tkinter import *
import math, random
from math import *

base = Tk()
base.title('Graphing calculator')
base.minsize(width = 300, height = 600)
base.maxsize(width = 300, height = 600)
base.configure(bg = 'gray')

frame = Frame(base, highlightthickness = 0, width = 300, height = 205, bg = 'gray')
frame.place(x = 0, y = 0)
grid = Canvas(base, bg = 'gray80', highlightthickness = 1, width = 280, height = 165)
grid.place(x = 10, y = 425)

def trim(string):
    new = ''
    for _ in (range(len(string))):
        if _ < len(string) - 1:
            new = str(new) + str(string[_])
    return new

class calculator():
    line1 = ''
    line2 = ''
    line3 = ''
    ans = 0
    others = {'MODE':'standard', 'FLOAT':8}
    screen = 'main'
    focus = 1
    LIN_EQ = 'y = x'
    def solve():
        try:
            exec(str('calculator.line2 = ' + str(calculator.line1)))
            calculator.ans = calculator.line2
        except: calculator.line2 = 'ERROR'
        calculator.main()
    def screenset(screen):
        calculator.focus = 1
        calculator.screen = str(screen)
        calculator.main()
    def appendC(character, line):
        if line == 1: calculator.line1 = str(calculator.line1) + str(character)
        elif line == 2: calculator.line2 = str(calculator.line2) + str(character)
        elif line == 3: calculator.line3 = str(calculator.line3) + str(character)
        calculator.main()
    def clear(line):
        calculator.line1 = ''
        calculator.line2 = ''
        calculator.line3 = ''
        calculator.main()
    def trim(line):
        if line == 1: calculator.line1 = trim(str(calculator.line1))
        elif line == 2: calculator.line2 = trim(str(calculator.line2))
        elif line == 3: calculator.line3 = trim(str(calculator.line3))
        calculator.main()
    def adjust(direction):
        if direction == 'S' and calculator.focus <= 2: calculator.focus += 1
        elif direction == 'N' and calculator.focus >= 2: calculator.focus -= 1
        calculator.main()
    def eval_linear():
        linear = str(calculator.LIN_EQ)
        x = 0
        y = 0
        x2 = 0
        y2 = 0
        if 'y = ' in linear:
            for _ in range(-140, 140):
                x = _
                exec(linear)
                grid.create_line(x, y, x2, y2, fill = 'black')
                x2 = x
                y2 = y
                print (y, x, x2, y2)
    def main():
        global frame, lin_eq
        lin_eq.destroy()
        lin_eq = Button(base, bg = 'gray80', text = str(calculator.LIN_EQ), font = 'Calibri 8', activebackground = 'green', activeforeground = 'black', fg = 'black', borderwidth = 0, command = lambda: calculator.eval_linear())
        lin_eq.place(x = 200, y = 395)
        frame.destroy()
        frame = Frame(base, highlightthickness = 0, width = 300, height = 205, bg = 'gray')
        frame.place(x = 0, y = 0)
        Canvas(frame, width = 290, height = 200, bg = 'black', highlightthickness = 0).place(x = 5, y = 5)
        Canvas(frame, width = 290, height = 30, bg = 'gray30', highlightthickness = 0).place(x = 5, y = 5)
        if calculator.screen == 'main' and calculator.focus <= 2 and calculator.focus >= 0 and calculator.focus != 'menu':
            Label(frame, font = 'Calibri 10', text = calculator.line1, bg = 'black', fg = 'white').place(x = 10, y = 60)
            Label(frame, font = 'Calibri 10', text = calculator.line2, bg = 'black', fg = 'white').place(x = 10, y = 80)
            Label(frame, font = 'Calibri 10', text = calculator.line3, bg = 'black', fg = 'white').place(x = 10, y = 100)
            Label(frame, font = 'Calibri 10', text = calculator.others, bg = 'gray30', fg = 'black').place(x = 10, y = 10)
            Label(frame, font = 'Calibri 10', text = '<---', bg = 'black', fg = 'white').place(x = 270, y = 60 + ((calculator.focus - 1) * 20))
        else:
            Label(frame, text = 'FOCUS: GRAPH', bg = 'gray30', fg = 'black').place(x = 10, y = 10)
    def begin():
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', width = 5, borderwidth = 0, command = lambda: calculator.screenset('settings'), text = 'MENU').place(x = 5, y = 215)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', width = 5, borderwidth = 0, command = lambda: calculator.screenset('main'), text = 'BACK').place(x = 95, y = 215)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'red', activeforeground = 'white', width = 5, borderwidth = 0, command = lambda: exit() or quit(), text = 'EXIT').place(x = 50, y = 215)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', width = 5, borderwidth = 0, command = lambda: calculator.clear(calculator.focus), text = 'CLR').place(x = 5, y = 245)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', width = 5, borderwidth = 0, command = lambda: calculator.trim(calculator.focus), text = 'DEL').place(x = 50, y = 245)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', width = 2, borderwidth = 0, command = lambda: calculator.appendC('(', calculator.focus), text = '(').place(x = 95, y = 245)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', width = 2, borderwidth = 0, command = lambda: calculator.appendC(')', calculator.focus), text = ')').place(x = 117, y = 245)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', text = '^', width = 2, borderwidth = 0, command = lambda: calculator.adjust('N')).place(x = 250, y = 220)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', text = 'v', width = 2, borderwidth = 0, command = lambda: calculator.adjust('S')).place(x = 250, y = 260)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', text = '<', width = 2, borderwidth = 0, command = lambda: calculator.adjust('W')).place(x = 230, y = 240)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', text = '>', width = 2, borderwidth = 0, command = lambda: calculator.adjust('E')).place(x = 270, y = 240)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = '7', command = lambda: calculator.appendC('7', calculator.focus)).place(x = 5, y = 275)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = '8', command = lambda: calculator.appendC('8', calculator.focus)).place(x = 40, y = 275)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = '9', command = lambda: calculator.appendC('9', calculator.focus)).place(x = 75, y = 275)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = '4', command = lambda: calculator.appendC('4', calculator.focus)).place(x = 5, y = 305)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = '5', command = lambda: calculator.appendC('5', calculator.focus)).place(x = 40, y = 305)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = '6', command = lambda: calculator.appendC('6', calculator.focus)).place(x = 75, y = 305)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = '1', command = lambda: calculator.appendC('1', calculator.focus)).place(x = 5, y = 335)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = '2', command = lambda: calculator.appendC('2', calculator.focus)).place(x = 40, y = 335)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = '3', command = lambda: calculator.appendC('3', calculator.focus)).place(x = 75, y = 335)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = '.', command = lambda: calculator.appendC('.', calculator.focus)).place(x = 5, y = 365)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = '0', command = lambda: calculator.appendC('0', calculator.focus)).place(x = 40, y = 365)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = '-', command = lambda: calculator.appendC(' - ', calculator.focus)).place(x = 75, y = 365)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = '+', command = lambda: calculator.appendC(' + ', calculator.focus)).place(x = 110, y = 275)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = '^', command = lambda: calculator.appendC(' ** ', calculator.focus)).place(x = 110, y = 305)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = '/', command = lambda: calculator.appendC(' / ', calculator.focus)).place(x = 110, y = 335)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = '*', command = lambda: calculator.appendC(' * ', calculator.focus)).place(x = 110, y = 365)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = 'abs', command = lambda: calculator.appendC('abs(', calculator.focus)).place(x = 145, y = 215)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = 'sin', command = lambda: calculator.appendC('sin(', calculator.focus)).place(x = 145, y = 245)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = 'cos', command = lambda: calculator.appendC('cos(', calculator.focus)).place(x = 145, y = 275)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = 'tan', command = lambda: calculator.appendC('tan(', calculator.focus)).place(x = 145, y = 305)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = 'pi', command = lambda: calculator.appendC('3.141592653589793', calculator.focus)).place(x = 145, y = 335)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = 'sqrt', command = lambda: calculator.appendC('sqrt(', calculator.focus)).place(x = 145, y = 365)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = 'ans', command = lambda: calculator.appendC('calculator.ans', calculator.focus)).place(x = 180, y = 365)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'green', activeforeground = 'white', width = 5, borderwidth = 0, command = lambda: calculator.solve(), text = 'SOLVE').place(x = 250, y = 365)
        Canvas(base, highlightthickness = 0, bg = 'gray80', width = 290, height = 200).place(x = 5, y = 395)
        Label(base, font = 'Calibri 8', text = 'Equation Graphing Area:', bg = 'gray80', fg = 'black').place(x = 5, y = 395)
        grid = Canvas(base, bg = 'gray80', highlightthickness = 1, width = 280, height = 165)
        grid.place(x = 10, y = 425)
        grid.create_line(140, 0, 140, 165, fill = 'black')
        grid.create_line(0, (165 / 2), 280, (165 / 2), fill = 'black')
        lin_eq = Button(base, bg = 'gray80', text = str(calculator.LIN_EQ), font = 'Calibri 8', activebackground = 'green', activeforeground = 'black', fg = 'black', borderwidth = 0, command = lambda: calculator.eval_linear())
        lin_eq.place(x = 200, y = 395)

grid = Canvas(base, bg = 'gray80', highlightthickness = 1, width = 280, height = 165)
grid.place(x = 10, y = 425)
grid.create_line(140, 0, 140, 165, fill = 'black')
grid.create_line(0, (165 / 2), 280, (165 / 2), fill = 'black')
lin_eq = Label(base, bg = 'gray80', text = str(calculator.LIN_EQ), font = 'Calibri 8')
lin_eq.place(x = 200, y = 395)
      
calculator.begin()
calculator.main()
base.mainloop()
