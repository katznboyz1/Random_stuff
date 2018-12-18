'''
Objective:
Make a function that returns an array that contains two integers that add up to the total number
'''

def getSums(integer):
    if (type(integer) == int):
        sums = []
        for numbers in range(integer):
            sums.append([numbers, (integer - numbers)])
        return sums
    else:
        raise ValueError('getSums() expected type {} but got {}.'.format(str(type(1)), str(type(integer))))

print(getSums(30))