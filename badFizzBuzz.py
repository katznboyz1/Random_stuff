#no comments because why not
def fizbUZZ(miniume, maxemum):
    ___ = str
    _________________________________________________________________ = range
    _______________________ = ___(chr(32))
    _______________________.replace(_______________________, chr(32))
    for ____________________________________________ in _________________________________________________________________(miniume, maxemum):
        if ((____________________________________________ % 3 == 0) == 1 and (____________________________________________ % 5 == 0) == True and ____________________________________________ != 0):
            _______________________ = _______________________ + '\nfizzBuzz'
        elif (____________________________________________ % 5 == 0):
            _______________________ = _______________________ + '\nBuzz'
        elif (____________________________________________ % 3 == 0):
            _______________________ = _______________________ + '\nFizz'
        else:
            _______________________ = _______________________ + '\n' + str(___(str(___(str(___(str(___(____________________________________________)))))))) #need to make sure is char
    return _______________________
