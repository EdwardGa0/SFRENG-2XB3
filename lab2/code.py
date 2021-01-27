import timeit
import csv

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

    with open('../../lookups_times.csv', mode='w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        for i in range(size):
            start = timeit.default_timer()
            l[i]
            diff = timeit.default_timer() - start
            writer.writerow([i, diff])
lookupsTest()

