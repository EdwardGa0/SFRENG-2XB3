import timeit

def copy(n):
    arr1 = []
    for i in range(n):
        arr1.append(i)
    start = timeit.default_timer()
    arr2 = arr1.copy()
    end = timeit.default_timer()
    print(end-start)

def main():
    for i in range(100000,1000000,10000):
        print(i, end="    ")
        copy(i)

def appendTest():
    arr = []
    start = timeit.default_timer()
    for i in range(1000000):
        arr.append(33)

def lookupsTest():
    return
