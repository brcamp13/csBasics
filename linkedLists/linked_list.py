# Linked list implementation 

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def size(self):
        """
        Returns number of data elements in list
        """
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next

        return count

    def empty(self):
        """
        Bool returns true if empty
        """
        if self.head:
            return True
        return False

    def value_at(self, index):
        """
        Returns the value of the nth item (starting at 0 for first)
        """
        temp = self.head
        count = 0

        while temp: 
            count += 1
            if count == index:
                return temp.value

        print("Index not in range")
        return -1

    def push_front(self, value):
        """
        Adds an item to the front of the list
        """
        new_node = ListNode(value)

        if self.empty():
            self.tail = new_node

        temp = self.head
        self.head = new_node
        new_node.next = temp
        
    def pop_front(self):
        """
        Remove the front item and return its value
        """
        if self.empty():
            print("Empty list")
            return -1

        value = self.head.value
        self.head = self.head.next
        return value

    def push_back(self, value):
        """
        Adds an item at the end of the list
        """
        new_node = ListNode(value)

        if self.empty():
            self.head = new_node

        temp = self.tail
        self.tail = new_node
        self.tail.prev = temp

    def pop_back(self):
        """
        Removes end item and returns its value
        """
        if self.empty():
            print("Empty list")
            return -1

        value = self.tail.value
        self.tail = self.tail.prev
        return value

    def front(self):
        """
        Get value of front item
        """
        if self.empty():
            print("Empty list")
            return -1

        return self.head.value

    def back(self):
        """
        Get value of end item
        """
        if self.empty():
            print("Empty list")
            return -1

        return self.tail.value

    def insert(self, index, value):
        """
        Insert value at index, so current item at that index
        is pointed to by new item at index
        """
        pass

    def erase(self, index):
        """
        Removes node at given index
        """
        pass

    def value_n_from_end(self, n):
        """
        Returns the value of the node at the nth position from the end 
        of the list
        """
        pass

    def reverse(self):
        """
        Reverses the list
        """
        pass

    def remove_value(self, value):
        """
        Removes the first item in the list with this value
        """
        pass


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
