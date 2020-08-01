result = []
flage = True
def from_base10(n, b):
    """This function is used for converting bases.
    param n: integer
    param b: integer
    return:  list
    """
    global flage

    if b < 2:
        raise ValueError ('Base must greater than 2.')

    if n < b and flage  == True:
        return result.insert(0,n)
    else:
        flage = False
        m , n = n % b, n // b
        result.insert(0,m)
        if n == 0:
            return [0]
        return from_base10(n, b)





from_base10(4,2)
print(result)
#help(from_base10)
