import timeit

def appendTest():
    arr = []
    start = timeit.default_timer()
    for i in range(1000000):
        arr.append(33)
