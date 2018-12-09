#At this point, there is no way to save the result into an image file.

import PyQt5 as PyQt5
from PyQt5.QtWidgets import *
import sys as sys
import _thread as thread
import os as os
import random as random

def event(eventType, debug = True): #disable <debug> for release
    global applicationRunning, pencolor, lineWidth, backgroundColor, renderView, textSize, textColor, textFont
    eventType = str(eventType)
    try:
        if (debug):
            print (eventType)
        if (eventType == 'exitProgram'):
            applicationRunning = False
            exit()
        elif (eventType.split(':')[0] == 'setcolor'):
            pencolor = str(eventType.split(':')[1])
        elif (eventType == 'canvasClear'):
            event('error\u2588Function not functional.')
        elif (eventType.split(':')[0] == 'setpw'):
            lineWidth = int(eventType.split(':')[1])
        elif (eventType.split(':')[0] == 'setbgndcolor'):
            backgroundColor = str(eventType.split(':')[1])
            renderView.setStyleSheet('QGraphicsView{background-color:' + backgroundColor + ';}')
        elif (eventType.split('\u2588')[0] == 'error'):
            errorDialog = QErrorMessage(window)
            errorDialog.showMessage(str(eventType.split('\u2588')[1]))
            errorDialog.setWindowTitle('Paint - Error')
    except Exception as err:
        event('error\u2588{}'.format(err))

applicationRunning = True

application = QApplication(sys.argv)

screen = application.primaryScreen()

window = QWidget()
window.setWindowTitle('Aesthetic label maker')
window.setStyleSheet('QWidget{background-color:white;}')
window.setMinimumSize(500, 300)
window.setWindowIcon(PyQt5.QtGui.QIcon('paint_application_icon.png'))
window.resize((screen.size().width() / 1.5), (screen.size().height() / 2))

pencolor = 'black'
lineWidth = 1
backgroundColor = 'white'
textFont = 'Calibri'
textSize = 20
textColor = 'black'

def paintEvent(x1, y1, x2, y2):
    global renderView, pencolor, lineWidth
    hwh = renderView.height() // 2
    hww = renderView.width() // 2
    y1 = (-y1)
    y2 = (-y2)
    x1 += 50
    x2 += 50
    a = QGraphicsLineItem(PyQt5.QtCore.QLineF(x1, y1, x2, y2))
    pen = PyQt5.QtGui.QPen(eval('PyQt5.QtCore.Qt.{}'.format(pencolor)))
    pen.setWidth(lineWidth)
    a.setPen(pen)
    renderView.scene().addItem(a)

def drawRect(xAnchor, yAnchor, width, height, fillcolor = '#ffffff'):
    xAnchor += 50
    global renderView
    height = (-height)
    a = QGraphicsRectItem(PyQt5.QtCore.QRectF(xAnchor, yAnchor, width, height))
    a.setBrush(PyQt5.QtGui.QColor(fillcolor))
    renderView.scene().addItem(a)

renderView = QGraphicsView(window)
renderView.move(0, 0)
renderView.setScene(QGraphicsScene(window))
renderView.setSceneRect(PyQt5.QtCore.QRectF(renderView.viewport().rect()))
renderView.setStyleSheet('QGraphicsView{background-color:' + backgroundColor + ';}')

mousePos = False
mouseXY = ''
mouseLastXy = ''

def generateBuilding(xAnchor, yAnchor, width, height):
    return [[xAnchor, yAnchor, xAnchor, (yAnchor + height)],
            [xAnchor, (yAnchor + height), (xAnchor + width), (yAnchor + height)],
            [(xAnchor + width), (yAnchor + height), (xAnchor + width), yAnchor],
            [(xAnchor + width), yAnchor, xAnchor, yAnchor],
           ]

colors = [
    '#400085', '#290054', '#5a02b8'
]

sunset = [
    [1, '#010c3b'],
    [2, '#010d40'],
    [3, '#021154'],
    [4, '#021878'],
    [5, '#0221ad'],
    [6, '#042de0'],
    [7, '#002fff'],
    [8, '#002fff'],
    [9, '#002fff'],
    [10, '#002fff'],
]

for color in sunset:
    drawRect(-window.width() / 2, (window.height() / 2) - ((window.height() / 10) * (10 - color[0])), window.width(), window.height() / 10, fillcolor = color[1])

for building in range(50):
    drawRect(random.choice([(random.randint(-window.width() / 2, window.width() / 2))]), (window.height() / 2), random.randint(100, 150), random.randint(50, 400), fillcolor = random.choice(colors))

label = QLabel(window)
label.setFixedWidth(window.width())
label.move(0, window.height() / 2)
label.setText('Hello world')
label.setStyleSheet('QLabel{background-color:transparent;color:white;font-family:Courier;font-size:50px;qproperty-alignment:AlignCenter;}')

def resizeThread():
    global applicationRunning, mouseLastXy, mousePos
    while (applicationRunning):
        renderView.resize(window.width(), window.height())
        label.setFixedWidth(window.width())
        label.move(0, window.height() / 2)

thread.start_new_thread(resizeThread, ())

window.show()

application.exec_()

applicationRunning = False

#I got fed up with QPainter so I didnt use it        ;-;