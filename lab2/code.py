import timeit

def appendTest():
    arr = []
    start = timeit.default_timer()
    for i in range(1000000):
        arr.append(33)

def lookupsTest():
    size = 1000000
    l = []
    for i in range(size):
        l.append(i)

    return l
