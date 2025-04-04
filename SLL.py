class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    
    def count(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
    def display(self):
        current = self.head
        while current:
            print(current.data,' -> ')
            current = current.next
        print("None")

    def delete(self, key):
        current = self.head
        prev = None
        if current and current.data == key:
            self.head = current.next
            return
        while current and current.data != key:
            prev = current
            current = current.next
        if not current:
            return
        prev.next = current.next
# Example Usage
'''
ll = SinglyLinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

ll.display()
print("Search 20:", ll.search(20))
print("Search 40:", ll.search(40))
print("Count:", ll.count())
'''