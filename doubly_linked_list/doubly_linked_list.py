"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
        as the new tail of the list. Don't forget to handle 
        the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        newNode = ListNode(value)
        if (self.length <= 0):
            self.head = newNode
            self.tail = newNode
            self.length += 1
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.length += 1

    def remove_from_tail(self):
        removed_node = self.tail
        # If we have an empty linked list
        if self.head is None and self.tail is None:
            return None
        else:
            if (self.length == 1):
                self.head = None
                self.tail = None
                self.length -= 1
            else:
                self.tail = self.tail.prev
                self.tail.next = None
                self.length -= 1
            return removed_node

    """Wraps the given value in a ListNode and inserts it 
        as the new head of the list. Don't forget to handle 
        the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        node = ListNode(value)
        if (self.length <= 0):
            self.head = node
            self.tail = node
            self.length += 1
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
            self.length += 1

    def remove_from_head(self):
        removed_node = self.head
        # If we have an empty linked list
        if self.head is None and self.tail is None:
            return None
        else:
            if (self.length == 1):
                self.head = None
                self.tail = None
                self.length -= 1
            else:
                self.head = self.head.next
                self.head.prev = None
                self.length -= 1
            return removed_node

    def move_to_front(self, node):
        if(self.length <= 0):
            return None
        if(self.head == node):
            return
        if(self.tail == node):
            self.tail = node.prev
        else:
            node.prev.next = node.next
        node.prev = None
        node.next = self.head
        self.head = node

        """Removes the input node from its current spot in the 
            List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if (self.length <= 0):
            return None
        if (self.tail == node):
            return
        if (self.head == node):
            self.head = node.next
            self.head.prev = None
            if (self.length == 2):
                self.head.next = node
        else:
            node.prev.next = node.next
        node.next = None
        node.prev = self.tail
        self.tail = node


    def get_max(self):
        if self.head is None:
            return None
        max_so_far = self.head.value
        current = self.head.next
        while current is not None:
            if current.value > max_so_far:
                max_so_far = current.value

        current = current.next
        return max_so_far

    """Removes a node from the list and handles cases where
       the node was the head or the tail"""

    def delete(self, node):
        if (node == self.head):
            self.remove_from_head()
        if (node == self.tail):
            self.remove_from_tail()
        else:
            node.delete()


    def print(self):
        # start at the head
        cur = self.head
        while cur:
            print(cur.value)
            cur = cur.next

# dllist = DoublyLinkedList()
# dllist.add_to_tail(1)
# dllist.add_to_tail(2)
# dllist.add_to_tail(3)
# dllist.add_to_tail(4)
#
# dllist.print()