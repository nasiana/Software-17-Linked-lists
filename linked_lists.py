# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ## AGENDA
# 
# 1. Introduction to Linked lists
# 2. Types of Linked lists
# 3. Linked list implementation
# 4. Practice and Exercises
# %% [markdown]
# ## Why do we need Linked lists?
# %% [markdown]
# Let's look at a simple list:
# 
# ```our_simple_list = [290, 401, 156, 374, 239]```
# 
# let's assume now that we want to insert a new element ```14``` at location 1. What Python does in a simple list when running that command, is to move all elements until the end of the list. 
# 
# ```our_simple_list.insert(1, 14)```
# 
# <div>
# <img src="insert_list_element.svg" width="500"/>
# </div>
# 
# %% [markdown]
# Array insertion space complexity = O(n)
# 
# What does this mean if we have 1 million elements? 
# %% [markdown]
# ```Linked lists``` makes the insertion and deletion of elements cheaper because the values are stored in different areas of memory (lists store the values in contiguous memory location). 
# 
# The values of a linked lists are stored at random memory location, but are linked with each other by **pointers**.
# %% [markdown]
# # Linked List
# 
# ## Singly Linked Lists
# 
# <div>
# <img src="slingly_linked_list.jpeg" width="500"/>
# </div>
# 
# <br>
# 
# ## Doubly Linked Lists
# 
# <div>
# <img src="double_linked_list.jpeg" width="500"/>
# </div>
# %% [markdown]
# ## Space complexity
# 
# | Operation                           | List | Linked List |
# | :-                                  | -:   | :-:         |
# | Indexing                            | O(1) | O(n)        |
# | Insert/Delete Element at Start      | O(n) | O(1)        |
# | Insert/Delete Element at End        | O(1) | O(1)        |
# | Insert/Delete Element at Middle     | O(n) | O(n)        |
# %% [markdown]
# ## Linked Lists Disadvantages
# 
# 1. Random access is not allowed. You have to access elements sequentially starting from the first node. 
# 2. Extra memory space for a pointer is required with each element of the list.
# 3. Not cache friendly.
# %% [markdown]
# ## Linked Lists vs Arrays
# 
# **Linked lists are preferable over arrays when:**
# 
# - you need constant-time insertions/deletions from the list (such as in real-time computing where time predictability is absolutely critical)
# - you don't know how many items will be in the list.
# - you don't need random access to any elements
# 
# **Arrays are preferable when:**
# 
# - you need indexed/random access to elements
# - you know the number of elements in the array ahead of time so that you can allocate the correct amount of memory for the array
# - you need speed when iterating through all the elements in sequence.
# - memory is a concern. Filled arrays take up less memory than linked lists. Each element in the array is just the data. Each linked list node requires the data as well as one (or more) pointers to the other elements in the linked list.
# %% [markdown]
# # Linked List Implementation

# %%
''' APPROACH 1 '''
class Node:
    def __init__(self, value, nextNode = None):
        self.value = value  # anything that you want to store (e.g., strings, integers, objects, etc)
        self.nextNode = nextNode #pointer to the next element in the linked list

# '3' -> '7' -> '10'

node_1 = Node('3')  # isolated node '3'
node_2 = Node('7')  # isolated node '7'
node_3 = Node('10') # isolated node '10'
node_4 = Node('77') # isolated node '77'

node_1.nextNode = node_2    # node_1 points to node_2, '3' -> '7' 
node_2.nextNode = node_3    # node_2 points to node_3, '7' -> '10' 

# node_1 -> node_2 -> node_3

# Let's test it out 
currentNode = node_1    # node_1 is our head 
while True: 
    print(currentNode.value, '-->', end=' ')
    if currentNode.nextNode is None:    # ensure that the current node is not tail
        print('None')
        break
    currentNode = currentNode.nextNode  # update with the next node 


# %%
''' APPROACH 2'''

class Node:
    def __init__(self, value, nextNode = None):
        self.value = value  # anything that you want to store (e.g., strings, integers, objects, etc)
        self.nextNode = nextNode #pointer to the next element in the linked list

class LinkedList:   # initially empty 
    def __init__(self, head = None):
        self.head = head 

    def insert(self, value):
        node = Node(value)  # create a node with the corresponding value 
        if self.head is None:   # check if there are other nodes 
            self.head = node    # if there are no other nodes, our current node is the head
            return 

        # look at the head node and try to find the tail by traversing
        #   the entire linked list 
        currentNode = self.head
        while True:
            # satisfied only if the current node is tail
            if currentNode.nextNode is None:    # if there is no node after the current node
                currentNode.nextNode = node     
                break
            currentNode = currentNode.nextNode      # otherwise, set the next to current node

    # method to print the linked list 
    def print_linked_list(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, '-->', end=' ')
            currentNode = currentNode.nextNode
        print('None')

ll = LinkedList()
ll.print_linked_list()
ll.insert('3')
ll.print_linked_list()
ll.insert('7')
ll.print_linked_list()
ll.insert('10')
ll.print_linked_list()

# %% [markdown]
# ## Linked Lists and Python 
# 
# Python does not have a linked list library built into it like some other programming languages so we need to create our own classes like above. However, there are some packages that can create data structures that behave as linked lists (but are not linked lists!), such as ```deque()```.

