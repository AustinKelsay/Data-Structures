class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        # the first Node in the LinkedList
        self.head = None
        # the last Node in the LinkedList
        self.tail = None

    def contains(self, data):
        # an empty linked list can't contain what we're looking for
        if not self.head:
            return False
        # get a reference to the first Node in the linked list
        # we update what this Node points to as we traverse the linked list
        current = self.head
        # traverse the linked list so long as `current` is referring
        # to a Node
        while current is not None:
            # check if the Node that `current` is pointing at is holding
            # the data we're looking for
            if current.get_value() == data:
                return True
            # update our `current` pointer to point to the next Node in the linked list
            current = current.get_next()

            # we checked the whole linked list and didn't find the data
            return False

    def get_max(self):
        if self.head is None:
            return None
        max_so_far = self.head.get_value()
        current = self.head.get_next()
        while current is not None:
            if current.get_value() > max_so_far:
                max_so_far = current.get_value()

        current = current.get_next()
        return max_so_far

    def add_to_tail(self, value):
        new_node = Node(value)
        # These three steps assume that the tail is already referring to a Node
        # So what do we do if tail is None?
        if self.tail is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # 1. create the node from the value
            # 2. set the old tail's next to refer to the new Node
            self.tail.set_next(new_node)
            # 3. reassign self.tail to refer to the new Node
            self.tail = new_node

    def remove_tail(self):
        # If we have an empty linked list
        if self.head is None and self.tail is None:
            return
        # if we have a non-empty linked list
        # Iterate over our linked list
        current = self.head
        while current.get_next() is not self.tail:
            current = current.get_next()
        # set the tail to be None
        val = self.tail.get_value()
        # move self.tail to the Node right before
        self.tail = current
        return val

    def remove_head(self):
        # If we have an empty linked list
        if self.head is None and self.tail is None:
            return
        # What if we only have a single elem in your linked list?
        # Both head and tail are pointing to the same Node
        if not self.head.get_next:
            head = self.head
            # delete the linked lists head reference
            self.head = None
            # Also delete the tail reference
            self.tail = None
            return head.get_value()
        # Normal condition
        val = self.head.get_value()
        # set self.head to the Node after the head
        self.head = self.head.get_next()
        return val
