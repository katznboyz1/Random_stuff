#improve UI

import PyQt5 as PyQt5
from PyQt5.QtWidgets import *
import sys as sys
import _thread as thread
import os as os
import urllib as urllib
import praw as praw
import shutil as shutil

application = QApplication(sys.argv)

screen = application.primaryScreen()

class app:
    appDefaultTitle = 'Title'
    appMinWidth = 500
    appMinHeight = 200
    applicationRunning = True
    windowState = 'min'

def event(e):
    e = str(e)
    if (e == 'exit'):
        app.applicationRunning = False
        exit()
    elif (e == 'minimizeWindow'):
        window.showMinimized()
    elif (e == 'toggleWindowSizeState'):
        if (app.windowState == 'min'):
            window.showMaximized()
            app.windowState = 'max'
        else:
            window.showNormal()
            app.windowState = 'min'
    elif (e.split('\u2588')[0] == 'setWindowTitle'):
        windowTitle.setText(e.split('\u2588')[1])
    elif (e.split('\u2588')[0] == 'error'):
        err = e.split('\u2588')[1]
        errorDialog = QErrorMessage(errWidget)
        errorDialog.showMessage(err)
        errorDialog.setWindowTitle('{} - Error'.format(app.defaultTitle))
        errorDialog.setStyleSheet('QErrorMessage{color:white;}')

window = QWidget()
window.setWindowTitle('Reddit App V2')
window.setStyleSheet('QWidget{background-color:#2b2b2b;}')
window.setWindowIcon(PyQt5.QtGui.QIcon('paint_application_icon.png'))
window.resize((screen.size().width() / 2), (screen.size().height() / 2))
window.setWindowFlags(PyQt5.QtCore.Qt.CustomizeWindowHint) 
window.setMinimumSize(app.appMinWidth, app.appMinHeight)

errWidget = QWidget(window)
errWidget.resize(0, 0)
errWidget.setStyleSheet('QWidget{background-color:white;}')

windowTopBorder = QWidget(window)
windowTopBorder.resize(window.width(), 20)
windowTopBorder.move(0, 0)
windowTopBorder.setStyleSheet('QWidget{background-color:black;}')
windowTopBorder.mousePressEvent = lambda e: headerMonitoring.windowDrag(e)
windowTopBorder.mouseMoveEvent = lambda e: headerMonitoring.windowMove(e)

windowTitle = QLabel(window)
windowTitle.move(10, 0)
windowTitle.setFixedHeight(20)
windowTitle.setStyleSheet('QLabel{color:white;font-family:Calibri;background-color:transparent;qproperty-alignment:AlignCenter;}')
windowTitle.mousePressEvent = lambda e: headerMonitoring.windowDrag(e)
windowTitle.mouseMoveEvent = lambda e: headerMonitoring.windowMove(e)
windowTitle.setFixedWidth(window.width())

exitButton = QPushButton(window)
exitButton.move((window.width() - exitButton.width()), 0)
exitButton.setText('X')
exitButton.resize(40, 20)
exitButton.setStyleSheet('''
QPushButton{background-color:transparent;color:white;font-family:Courier;}
QPushButton:hover{background-color:red;color:white;font-family:Courier;}
''')
exitButton.clicked.connect(lambda: event('exit'))

toggleWindowStateButton = QPushButton(window)
toggleWindowStateButton.move((exitButton.x() - exitButton.width()), 0)
toggleWindowStateButton.setText('[]')
toggleWindowStateButton.resize(40, 20)
toggleWindowStateButton.setStyleSheet('''
QPushButton{background-color:transparent;color:white;font-family:Courier;}
QPushButton:hover{background-color:#6b6a6a;color:white;font-family:Courier;}
''')
toggleWindowStateButton.clicked.connect(lambda: event('toggleWindowSizeState'))

minimizeButton = QPushButton(window)
minimizeButton.move((toggleWindowStateButton.x() - toggleWindowStateButton.width()), 0)
minimizeButton.setText('-')
minimizeButton.resize(40, 20)
minimizeButton.setStyleSheet('''
QPushButton{background-color:transparent;color:white;font-family:Courier;}
QPushButton:hover{background-color:#6b6a6a;color:white;font-family:Courier;}
''')
minimizeButton.clicked.connect(lambda: event('minimizeWindow'))

def resizeThread():
    while (app.applicationRunning):
        exitButton.move((window.width() - exitButton.width()), 0)
        toggleWindowStateButton.move((exitButton.x() - exitButton.width()), 0)
        minimizeButton.move((toggleWindowStateButton.x() - toggleWindowStateButton.width()), 0)
        windowTopBorder.resize(window.width(), 20)
        windowTitle.setFixedWidth(window.width())

thread.start_new_thread(resizeThread, ())

event('setWindowTitle\u2588{}'.format(app.appDefaultTitle))

window.show()

application.exec_()

applicationRunning = False

for file in os.listdir('./tmp'):
    os.remove('./tmp/' + file)