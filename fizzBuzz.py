'''
Problem:
Write a program that prints number from the range x to y but for multiples
of three print "fizz" instead of the number and instead of multpiples of 5
print "buzz" and for numbers with multpiles of moth print fizzBuzz.
'''

def fizzBuzz(MIN, MAX):
    string = ''
    for number in range(MIN, MAX):
        if (number % 3 == 0 and number % 5 == 0 and number != 0):
            string += '\nFizzBuzz'
        elif (number % 3 == 0):
            string += '\nFizz'
        elif (number % 5 == 0):
            string += '\nBuzz'
        else:
            string += '\n{}'.format(str(number))
    return string

print (fizzBuzz(0, 100))