# Manual implementation of a dynamic list/array

class MutableArray:

    def __init__(self):
        self.array = [None] * 16
        self.capacity = 16
        self.size = 0

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

    def is_empty(self):
        return self.size == 0

    def at(self, index):
        if index > capacity-1:
            print("Index out of range error")
            return -1
        return self.array[index]

    def push(self, item):
        if self.size < self.capacity:
            self.array[size] = item
            size += 1
        else:
            new_array = [None] * (self.capacity * 2)
            for value in self.array:
                new_array.append(value)
            new_array.append(item)
            size += 1
            self.capacity *= 2

    def insert(self, index, item):
        