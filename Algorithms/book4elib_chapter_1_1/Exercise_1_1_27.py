import datetime


def binomial(n, k, p):
    if n == 0 and k == 0:
        return 1.0
    if n < 0 or k < 0:
        return 0.0
    return (1 - p) * binomial(n - 1, k, p) + p * binomial(n - 1, k - 1, p)


def binomial_upgraded(n, k, p, mydict):
    if n == 0 and k == 0:
        return 1.0
    if n < 0 or k < 0:
        return 0.0

    if mydict.get(str(n - 1) + "," + str(k)) is None:
        mydict[str(n - 1) + "," + str(k)] = binomial_upgraded(n - 1, k, p, mydict)

    if mydict.get(str(n - 1) + "," + str(k - 1)) is None:
        mydict[str(n - 1) + "," + str(k - 1)] = binomial_upgraded(n - 1, k - 1, p, mydict)

    return (1 - p) * mydict[str(n - 1) + "," + str(k)] + p * mydict[str(n - 1) + "," + str(k - 1)]


firstTime = datetime.datetime.now()
# print("The binomial(30, 10, 0.25) : ", binomial(30, 15, 0.25))
print("The binomial(30, 10, 0.25) : ", binomial_upgraded(30, 15, 0.25, dict()))
secondTime = datetime.datetime.now()
print("The completed time in seconds: ", (secondTime - firstTime).seconds)
