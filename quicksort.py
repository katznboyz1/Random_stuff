class sorter:
    sortException = Exception
    def sort(__list__) -> list: #sorts numbers in a list from min to max
        if type(__list__) == list:
            pass
        else:
            raise sorter.sortException('The value given to <sorter.sort> was not a list. This program only sorts lists.')
        finalList = __list__
        tmplist1 = []
        while (not sorter.isSorted(finalList)):
            for each in range(len(finalList)):
                if (each + 1 >= len(finalList)):
                    pass
                else:
                    if (finalList[each] >= finalList[each + 1]):
                        finalList[each], finalList[each + 1] = finalList[each + 1], finalList[each]
        return finalList
    def isSorted(__list__) -> bool: #checks that list is sorted from min to max
        if type(__list__) == list:
            pass
        else:
            raise sorter.sortException('The value given to <sorter.sort> was not a list. This program only sorts lists.')
        ISSORTED = True
        last = __list__[0]
        for each in __list__:
            if (each >= last):
                pass
            else:
                ISSORTED = False
            last = each
        return ISSORTED