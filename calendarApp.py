import sys as sys
import time as time
from time import localtime

args = sys.argv[1:]

class application:
    class variables:
        calendar = []
        appRunning = True
        commands = ['exit', 'add']
    def interperetCommand(command):
        command = str(command)
        commands = command.split(' ')
        try:
            if (commands[0] in application.variables.commands):
                for command_ in application.variables.commands:
                    if (command_ == 'exit'):
                        application.variables.appRunning = False
                    if (command_ == 'add'):
                        if (len(commands) > 1):
                            if (commands[1] == 'event'):
                                eventType = input('Input a name for the event below:\n')
                                eventDate = input('Input the day for the event (DD/MM/YYYY) below:\n')
                                eventTime = input('Input the time for the event (HH:MM) in 24 hour time below:\n')
                                validEntry = True
                                if (eventDate.count('/') == 2):
                                    pass
                                else:
                                    print ('Invalid entry for event date: {}'.format(eventDate))
                                    validEntry = False
                                if (eventTime.count(':') == 1):
                                    pass
                                else:
                                    print ('Invalid entry for event time: {}'.format(eventTime))
                                    validEntry = False
                                if (validEntry):
                                    print ('Event added to your calendar.')
                                    application.variables.calendar.append([eventType, eventDate, eventTime])
            else:
                print ('Invalid command: {}'.format(commands[0]))
        except Exception as err:
            print (err)
    class applicationBaseExecError(Exception):
        pass

if (args != []):
    command = ''
    for iteration in range(len(args)):
        command += str(args[iteration] + ' ')
    application.interperetCommand(command)
else:
    while (application.variables.appRunning):
        try:
            application.interperetCommand(input('calendarApp> '))
        except EOFError or KeyboardInterrupt:
            application.variables.appRunning = False
    print ('\n\nExiting')
    