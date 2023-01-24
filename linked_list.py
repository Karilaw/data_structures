# tutorial on linked lists
# implementation of linked list in python

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_begging(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '<---->'
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, datalist):
        self.data = None
        for data in datalist:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception('invalid index')

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid Index')

        if index == 0:
            self.insert_at_begging(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1


ll = LinkedList()
ll.insert_values(['lawrence', 'martin', 'kevin', 'mark', 'derrick'])
ll.print()
ll.remove_at(2)
ll.insert_at(2, 'Kimendu')
ll.print()
print('length of LL: ',  ll.get_length())

# In LinkedList class that we implemented in our tutorial add following two methods,
# def insert_after_value(self, data_after, data_to_insert):
#     # Search for first occurance of data_after value in linked list
#     # Now insert data_to_insert after data_after node

# def remove_by_value(self, data):
#     # Remove first node that contains data
# Now make following calls,

#     ll = LinkedList()
#     ll.insert_values(["banana","mango","grapes","orange"])
#     ll.print()
#     ll.insert_after_value("mango","apple") # insert apple after mango
#     ll.print()
#     ll.remove_by_value("orange") # remove orange from linked list
#     ll.print()
#     ll.remove_by_value("figs")
#     ll.print()
#     ll.remove_by_value("banana")
#     ll.remove_by_value("mango")
#     ll.remove_by_value("apple")
#     ll.remove_by_value("grapes")
#     ll.print()


def insert_after_value(self, data_after, data_to_insert):
    if data_after < 0 or data_after > self.
