from tkinter import *
import random

grid = Tk()
grid.title('Packet Reviver')

def unpack(PACKETS, RESOLUTION): #RESOLUTION = [WIDTH, HEIGHT]
    ITEM = 0
    for __ in range(RESOLUTION[1]):
        for _ in range(RESOLUTION[0]):
            Label(grid, bg = str(PACKETS.split('|')[ITEM]), width = 1).place(x = (_ * 12), y = (__ * 20))
            ITEM += 1
packets = ''

def main():
    global packets
    COLORS = ['black', 'gray', 'white']
    packets = ''
    for _ in range(3400):
        packets = str(packets) + str(random.choice(COLORS)) + '|'
    unpack(packets, [100, 34])
    #grid.after(1000, lambda: main())

main()
grid.mainloop()

