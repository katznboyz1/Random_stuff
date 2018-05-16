try: from tkinter import *
except ImportError: input('Tkinter is not installed.')
try: import random
except ImportError: input('Module "random" is not installed.')

#RES = [int(input('H:')), int(input('W:'))]
RES = [540, 300]
PIX = ''

print ('Creating map...')

for _ in range(0, (RES[0] * RES[1])): PIX = str(PIX) + '|' + str(random.choice(['black', 'white']))

monitor = Tk()
monitor.title((str(RES[0]) + 'x' + str(RES[1])))
monitor.minsize(width = RES[0], height = RES[1])
monitor.maxsize(width = RES[0], height = RES[1])

screen = Canvas(monitor, highlightthickness = 0, width = RES[0], height = RES[1], bg = 'black')
screen.place(x = 0, y = 0)

def BLIT(MAP, MAP_SEPERATOR, RESOLUTION, ANCHOR):
    MAP = MAP.split(str(MAP_SEPERATOR))
    POS = [0, 0, 0,  0]
    for H in range(RESOLUTION[1]):
        for W in range(RESOLUTION[0]):
            POS[0] = W
            POS[1] = H
            POS[2] = W + 1
            ANCHOR.create_line(POS[0], POS[1], POS[2], POS[1], fill = MAP[(POS[3])])
            POS[3] += 1

print('Blitting map...')

BLIT(PIX, '|', RES, screen)

monitor.mainloop()
