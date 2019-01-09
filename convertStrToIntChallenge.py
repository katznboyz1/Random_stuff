#Challenge:
#Convert a string to an integer without using the <str> or <int> classes

def stringTOint(string):
    integer = eval(string)
    return integer

def intTOstring(integer):
    string = eval('"{}"'.format(integer))
    return string

def test():
    print (stringTOint('123') + stringTOint('123'))
    print (intTOstring(123) + intTOstring(123))