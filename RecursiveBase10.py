result = []
def from_base10(n, b):
    if b < 2:
        raise ValueError ('Base must greater than 2.')

    #m = n % b
    #n = n // b
    m , n = n % b, n // b
    result.insert(0,m)
    print(n)
    if n == 0:
        return [0]
    return from_base10(n, b)

from_base10(4,2)
print(result)
