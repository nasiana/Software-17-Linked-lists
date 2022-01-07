"""
TASK

Find the length of a linked list.
A user should enter the elements of the linked list to create and then displays its length.

Steps:
1. Create a class Node.
2. Create a class LinkedList.
3. Define method append inside the class LinkedList to append data to the linked list.
4. Define method length.
5. The method length uses a loop to iterate over the nodes of the list to calculate its length.
6. Create an instance of LinkedList and prompt the user for its elements.
7. Display the length of the list by calling the method length.

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def length(self):
        current = self.head
        length = 0
        while current:
            length = length + 1
            current = current.next
        return length


###############################

## RUNNER

"""
Case 1:
Please enter the elements in the linked list: 5 10
The length of the linked list is 2.
  
Case 2:
Please enter the elements in the linked list: 11 4 100 5
The length of the linked list is 4.
"""

llist = LinkedList()
data_list = input('Please enter the elements in the linked list: ').split()

for data in data_list:
    llist.append(int(data))

print('The length of the linked list is ' + str(llist.length()) + '.', end='')
