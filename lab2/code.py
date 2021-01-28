import timeit
import csv

def copy(n):
    arr1 = []
    for i in range(n):
        arr1.append(i)
    start = timeit.default_timer()
    arr2 = arr1.copy()
    end = timeit.default_timer()
    print(end-start)

def main():
    for i in range(100000,10000000,100000):
        print(i, end="    ")
        copy(i)

def appendTest():
    arr = []
    f1 = open('./append.txt', 'w')
    f2 = open('./append2.txt', 'w')
    time_sum = 0
    for i in range(1000000):
        start = timeit.default_timer()
        arr.append(33)
        end = timeit.default_timer()
        time_sum += end - start
        f1.write(str(i) + ', ' + str(time_sum) + '\n')
        f2.write(str(i) + ', ' + str(end - start) + '\n')
    f1.close()
    f2.close()
    




def lookupsTest():
    size = 1000000
    l = []
    for i in range(size):
        l.append(0)

    with open('../../lookups_times.csv', mode='w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        for i in range(size):
            start = timeit.default_timer()
            l[i]
            diff = timeit.default_timer() - start
            writer.writerow([i, diff])

appendTest()