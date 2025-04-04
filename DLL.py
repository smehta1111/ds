class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def show(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def show_reverse(self):
        temp = self.tail
        while temp:
            print(temp.data)
            temp = temp.prev

dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)

dll.show()
# Output:
# 10
# 20
# 30

dll.show_reverse()
# Output:
# 30
# 20
# 10
