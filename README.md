# data_structures

A linked list is a data structure that shows how nodes are connected in a sequence.
like stacks and ques the memory of linked list is not sequential.
Each node in linked list cointains two parts

> a data part and adress part which holds the adress of next node
> The advantage of ll over stacks and queues is that inserion and deletion is easier.
> and there is no need to pre-allocate memory.

a class for creating node in linked list

class Node:
def **\_init**(self, data=None, next=node):
self.data = data
self.next = next

Now that we have created the node we have to implement all the functionalities in LinkedList class:
All methods are described inside Linked list class

class LinkedList(self):
def **init**(self)
self.head = None

A fuction to insert element at the beginning:

def insert_element_at_begging(self, data):
node = Node(data, self.head)
self.head = node

A fuction to insert element at the end:

def insert_element_at_end(self, data, next):
if self.head is None:
self.head = Node(data, self.head)
else:
itr = self.head
While itr.next:
itr.next
itr.next = Node(data, None)

while the user sends mutiple elements, we convert the elements in list and insert them at the end of linked list using insert_element_at_end.

def insert_elements_end(self, data_list):
self.head = None
for data in data_list:
self.insert_at_end(data)

Let us now define a function that counts the number of nodes present in the LinkedList by traversing the whole list of elements.

def get_length(self):
count = 0
itr = self.head
while itr.next
count += 1
itr = itr.next
return count
