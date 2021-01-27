import timeit

def appendTest():
    arr = []
    f = open('./append.txt', 'w')
    time_sum = 0
    for i in range(1000000):
        start = timeit.default_timer()
        arr.append(33)
        end = timeit.default_timer()
        time_sum += end - start
        f.write(str(i) + ', ' + str(time_sum) + '\n')



def lookupsTest():
    return

appendTest()