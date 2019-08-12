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
        if index > self.capacity-1:
            print("Index out of range error")
            return -1
        return self.array[index]

    def push(self, item):
        if self.size < self.capacity:
            self.array[self.size] = item
            self.size += 1
        else:
            self.resize(self.capacity*2)
            self.size += 1
            self.capacity *= 2

    def insert(self, index, item):
        for i in range(len(self.array)-1, index, -1):
            temp = self.array[i]
            self.array[i+1] = temp
        self.array[index] = item

    def prepend(self, item):
        self.insert(0, item)

    def pop(self):
        item = self.array[-1]
        self.array.remove()
        return item

    def delete(self, index):
        for i in range(index, len(self.array) - 1):
            self.array[index] = self.array[i+1]

    def remove(self, item):
        for i in range(0, len(self.array)):
            if self.array[i] == item: 
                self.delete(i)

    def find(self, item):
        for i in range(0, len(self.array)):
            if self.array[i] == item:
                return i
        return -1

    def resize(self, new_capacity):
        new_array = [None] * (new_capacity)
        for value in self.array:
            new_array.append(value)
