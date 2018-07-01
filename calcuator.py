#GRAPHING CALCULATOR SCRIPT COPYLEFT HARRISON LINDGREN <harrison.lindgren@gmail.com>

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
    others = {'MODE':'standard', 'FLOAT':8}
    screen = 'main'
    focus = 1
    def solve():
        try: exec(str('calculator.line2 = ' + str(calculator.line1)))
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
        if line == 1: calculator.line1 = ''
        elif line == 2: calculator.line2 = ''
        elif line == 3: calculator.line3 = ''
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
    def main():
        global frame
        frame.destroy()
        frame = Frame(base, highlightthickness = 0, width = 300, height = 205, bg = 'gray')
        frame.place(x = 0, y = 0)
        Canvas(frame, width = 290, height = 200, bg = 'black', highlightthickness = 0).place(x = 5, y = 5)
        Canvas(frame, width = 290, height = 30, bg = 'gray30', highlightthickness = 0).place(x = 5, y = 5)
        if calculator.screen == 'main':
            Label(frame, font = 'Calibri 10', text = calculator.line1, bg = 'black', fg = 'white').place(x = 10, y = 60)
            Label(frame, font = 'Calibri 10', text = calculator.line2, bg = 'black', fg = 'white').place(x = 10, y = 80)
            Label(frame, font = 'Calibri 10', text = calculator.line3, bg = 'black', fg = 'white').place(x = 10, y = 100)
            Label(frame, font = 'Calibri 10', text = calculator.others, bg = 'gray30', fg = 'black').place(x = 10, y = 10)
            Label(frame, font = 'Calibri 10', text = '<---', bg = 'black', fg = 'white').place(x = 270, y = 60 + ((calculator.focus - 1) * 20))
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
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = '-', command = lambda: calculator.appendC('-', calculator.focus)).place(x = 75, y = 365)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = '+', command = lambda: calculator.appendC('+', calculator.focus)).place(x = 110, y = 275)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = '^', command = lambda: calculator.appendC('**', calculator.focus)).place(x = 110, y = 305)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = '/', command = lambda: calculator.appendC('/', calculator.focus)).place(x = 110, y = 335)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = '*', command = lambda: calculator.appendC('*', calculator.focus)).place(x = 110, y = 365)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = 'abs', command = lambda: calculator.appendC('abs(', calculator.focus)).place(x = 145, y = 215)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = 'sin', command = lambda: calculator.appendC('sin(', calculator.focus)).place(x = 145, y = 245)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = 'cos', command = lambda: calculator.appendC('cos(', calculator.focus)).place(x = 145, y = 275)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = 'tan', command = lambda: calculator.appendC('tan(', calculator.focus)).place(x = 145, y = 305)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = 'ord', command = lambda: calculator.appendC('ord(', calculator.focus)).place(x = 145, y = 335)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'gray12', activeforeground = 'white', borderwidth = 0, width = 3, text = 'chr', command = lambda: calculator.appendC('chr(', calculator.focus)).place(x = 145, y = 365)
        Button(base, bg = 'gray12', fg = 'white', activebackground = 'green', activeforeground = 'white', width = 5, borderwidth = 0, command = lambda: calculator.solve(), text = 'SOLVE').place(x = 250, y = 365)
        Canvas(base, highlightthickness = 0, bg = 'gray80', width = 290, height = 200).place(x = 5, y = 395)
        
calculator.begin()
calculator.main()
base.mainloop()
