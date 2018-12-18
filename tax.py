def tax(total, tax):
    if (tax > 1 or tax < 0):
        raise Exception('Value for argument <tax> has to be a decimal between 0 and 1.')
    else:
        ttl = (total * tax)
        return ttl
