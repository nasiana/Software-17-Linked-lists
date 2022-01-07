"""
NODE
The node is where data is stored in the linked list.
Each node also holds a pointer, which is a reference to the next node in the list.
"""


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


"""
LINKED LIST

This implementation includes the following methods:
- Insert: inserts a new node into the list
- Size: returns size of list
- Search: searches list for a node containing the requested data and returns that node if found.
- Delete: searches list for a node containing the requested data and removes it from list if found.
"""


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next_node
        nodes.append("None")
        return " -> ".join(nodes)

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


"""
IMPLEMENTATION
"""

llist = LinkedList()
print(llist)

n1 = Node('a')
llist.head = n1
print(llist)

n2 = Node('b')
n3 = Node('c')
n1.set_next(n2)
n2.set_next(n3)
print(llist)
print(llist.size())
