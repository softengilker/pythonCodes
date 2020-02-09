def gcd(n1, n2):

    mod = n1 % n2

    if mod == 0:
        return n2

    return gcd(n2, mod)


def create_array(n1, n2):

    a = [[False for x in range(n1)] for y in range(n2)]

    for x in range(n2):
        for y in range(n1):
            if gcd(x + 1, y + 1) == 1:
                a[x][y] = True

    return a


print(create_array(2, 3))
