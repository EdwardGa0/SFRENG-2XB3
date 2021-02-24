import math

class KHeap:
    length = 0
    data = []

    def __init__(self, values, k):
        self.data = values
        self.length = len(values)
        self.k = k
        self.build_heap()

    def build_heap(self):
        for i in range(self.length // self.k + 1, -1, -1):
            self.sink(i)

    def sink(self, i):
        largest_known = i
        for j in self.children(i):
            if j < self.length and self.data[j] > self.data[largest_known]:
                largest_known = j
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.sink(largest_known)

    def insert(self, value):
        if len(self.data) == self.length:
            self.data.append(value)
        else:
            self.data[self.length] = value
        self.length += 1
        self.swim(self.length - 1)

    def insert_values(self, L):
        for num in L:
            self.insert(num)

    def swim(self, i):
        while i > 0 and self.data[i] > self.data[self.parent(i)]:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            i = self.parent(i)

    def extract_max(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        max_value = self.data[self.length - 1]
        self.length -= 1
        self.sink(0)
        return max_value

    def children(self, i):
        return [j for j in range(i * self.k + 1, i * self.k + self.k + 1)]

    def parent(self, i):
        return (i + k - 1) // k - 1

    def __str__(self):
        o = ""
        for i in range(len(self.data)):
            if (i < self.length):
                o += str(self.data[i]) + " "
        return o

b = [-4,5,11111,7,23,5576,3,3,-123,54,11111111]
a = KHeap(b, 5)
print(a)