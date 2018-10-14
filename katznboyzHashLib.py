class katznboyzHashLib():
    def hash(string):
        string = str(string)
        hashval = 0
        for iteration in string:
            v1 = ord(iteration)
            v2 = v1 + len(string)
            v3 = v1 + v2
            hashval = hashval + v3 * v3
        return (hashval * hashval)
    def help():
        return '''
HELP FOR CLASS <katznboyzHashLib>

katznboyzHashLib {
    hash {
        Returns an individual integer that can be used to represend a string.
        Example: katznboyzHashLib.hash("foo")
    }
    help {
        Prints out the help menu for this class.
    }
}
'''