#this script is for a 320x240 screen

from odroid_go import GO
import time

try:
    GO.lcd.set_font(GO.lcd.fonts.TT14)
    GO.lcd.erase()
    GO.lcd.print('Starting...')
    GO.lcd.set_pos(0, 0)

    class calculator:
        int1 = 0
        int2 = 0
        lastInt1 = 0
        lastInt2 = 0
        operation = '+'
        equation = ''
        lastoperation = ''
        isrunning = True
        stage = 'homescreen'
        lastStage = ''
        answer = 0
        stages = ['homescreen', 'chooseOperation', 'chooseInt1', 'chooseInt2', 'answer']

    while (calculator.isrunning):
        GO.update()
        GO.lcd.set_pos(0, 0)
        if (GO.btn_start.is_pressed() == 1):
            calculator.stage = 'homescreen'
        if (calculator.stage == 'homescreen' and calculator.lastStage == 'homescreen'):
            if (GO.btn_a.is_pressed() == 1):
                calculator.stage = 'chooseOperation'
        if (calculator.stage == 'chooseOperation' and calculator.lastStage == 'chooseOperation'):
            if (GO.btn_joy_x.is_axis_pressed() == 1):
                if (calculator.operation == '+'):
                    calculator.operation = '-'
                elif (calculator.operation == '-'):
                    calculator.operation = '**'
                elif (calculator.operation == '**'):
                    calculator.operation = '*'
                else:
                    calculator.operation = '+'
            if (GO.btn_a.is_pressed() == 1):
                calculator.stage = 'chooseInt1'
        if (calculator.stage == 'chooseInt1' and calculator.lastStage == 'chooseInt1'):
            if (GO.btn_joy_y.is_axis_pressed() == 2):
                calculator.int1 += 1
            elif (GO.btn_joy_y.is_axis_pressed() == 1):
                calculator.int1 -= 1
            if (GO.btn_a.is_pressed() == 1):
                calculator.stage = 'chooseInt2'
        if (calculator.stage == 'chooseInt2' and calculator.lastStage == 'chooseInt2'):
            if (GO.btn_joy_y.is_axis_pressed() == 2):
                calculator.int2 += 1
            elif (GO.btn_joy_y.is_axis_pressed() == 1):
                calculator.int2 -= 1
            if (GO.btn_a.is_pressed() == 1):
                calculator.stage = 'answer'
        if (calculator.lastStage != calculator.stage):
            if (calculator.stage in calculator.stages):
                if (calculator.stage == 'homescreen'):
                    GO.lcd.erase()
                    GO.lcd.print('''
    Simple ODROID-GO calculator by katznboyz. Keys are as follow:
    START - Reset the calculator and go to home screen.
    UP_KEY - Increase value
    DOWN_KEY - Decrease value
    RIGHT_KEY - Move right
    LEFT_KEY - Delete last character
    B - Not assigned
    A - Next screen
    ---Press A to begin---
    ''')
                    calculator.int1 = 0
                    calculator.int2 = 0
                    calculator.operation = '+'
                    calculator.equation = ''
                if (calculator.stage == 'chooseOperation'):
                    GO.lcd.erase()
                    GO.lcd.print('Choose the operation, here is a list of choices:\n+(plus) -(minus) **(exponent) *(times) /(divide)\nUse the right arrow to switch between the choices.')
                    GO.lcd.print('Current operation:    {}'.format(calculator.operation))
                if (calculator.stage == 'chooseInt1'):
                    GO.lcd.erase()
                    GO.lcd.print('Choose the first integer. Press the up button to increase the value and press the down button to decrease the value.')
                    GO.lcd.print('Current choice:     {}'.format(str(calculator.int1)))
                if (calculator.stage == 'chooseInt2'):
                    GO.lcd.erase()
                    GO.lcd.print('Choose the second integer. Press the up button to increase the value and press the down button to decrease the value.')
                    GO.lcd.print('Current choice:     {}'.format(str(calculator.int2)))
                if (calculator.stage == 'answer'):
                    calculator.equation = str(str(calculator.int1) + str(calculator.operation) + str(calculator.int2))
                    calculator.answer = str(eval(calculator.equation))
                    GO.lcd.erase()
                    GO.lcd.print(calculator.equation)
                    GO.lcd.print(calculator.answer)
            elif (calculator.stage not in calculator.stages and calculator.stage != calculator.lastStage):
                GO.lcd.erase()
                GO.lcd.print('Fatal error: Unknown screen - "{}"'.format(calculator.stage))
                calculator.stage == 'ERROR'
        if (calculator.stage == 'chooseOperation' and calculator.operation != calculator.lastoperation):
            GO.lcd.erase()
            GO.lcd.print('Choose the operation, here is a list of choices:\n+(plus) -(minus) **(exponent) *(times) /(divide)\nUse the right arrow to switch between the choices.')
            GO.lcd.print('Current operation:    {}'.format(calculator.operation))
        if (calculator.stage == 'chooseInt1' and calculator.int1 != calculator.lastInt1):
            GO.lcd.erase()
            GO.lcd.print('Choose the first integer. Press the up button to increase the value and press the down button to decrease the value.')
            GO.lcd.print('Current choice:     {}'.format(str(calculator.int1)))
        if (calculator.stage == 'chooseInt2' and calculator.int2 != calculator.lastInt2):
            GO.lcd.erase()
            GO.lcd.print('Choose the second integer. Press the up button to increase the value and press the down button to decrease the value.')
            GO.lcd.print('Current choice:     {}'.format(str(calculator.int2)))
        calculator.lastStage = calculator.stage
        calculator.lastoperation = calculator.operation
        calculator.lastInt1 = calculator.int1
        calculator.lastInt2 = calculator.int2
except Exception as err:
    GO.lcd.print(err)
