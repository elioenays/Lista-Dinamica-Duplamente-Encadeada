class Node():
    def __init__(self, data, previous, next):
        self.data = data
        self.prev = previous
        self.next = next


class DoubleList():
    def __init__(self):
        self.head = Node(None, None, None)
        self.last = Node(None, None, None)

        self.last.prev = self.head
        self.head.next = self.last

        self._size = 0

    def insert_initial(self, value):
        new_node = Node(value, self.head, self.head.next)

        self.head.next.prev = new_node
        self.head.next = new_node

        self._size += 1

        return new_node

    def insert_end(self, value):
        new_node = Node(value, self.last.prev, self.last)

        self.last.prev.next = new_node
        self.last.prev = new_node

        self._size += 1

        return new_node

    def remove_initial(self):
        if self._size == 1:
            self.head.next = self.last
            self.last.prev = self.head

        else:
            node = self.head.next
            nextNode = node.next

            nextNode.prev = self.head
            self.head.next = nextNode

    def remove_end(self):
        if self._size == 1:
            self.head.next = self.last
            self.last.prev = self.head

        else:
            node = self.last.prev
            prev = node.prev

            prev.next = self.last
            self.last.prev = prev

    def show(self):
        temp = self.head.next
        list = []

        while temp.next != None:
            list.append(temp.data)
            temp = temp.next

        return list


doubleList = DoubleList()

doubleList.insert_initial(11)
doubleList.insert_end(12)
doubleList.insert_end(24)
doubleList.insert_initial(1)
doubleList.insert_end(34)

print(doubleList.show())
doubleList.remove_initial()
doubleList.remove_end()
print(doubleList.show())
