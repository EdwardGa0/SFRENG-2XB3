import timeit

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
        l.append(i)

    times = []
    for i in range(size):
        start = timeit.default_timer()
        l[i]
        diff = timeit.default_timer() - start
        times.append(diff)

appendTest()