class LinkedList:
    def __init__(self, collection=None):
        self.head = None
        self.length = 0
        if collection:
            for item in reversed(collection):
                self.insert(item)

    def __iter__(self):
        def generator():
            current = self.head
            while current:
                yield current.value

                current = current.next

        return generator()

    def __str__(self):
        string = ""

        for value in self:
            string += f"[ {value} ] -> "

        return string + "None"

    def __len__(self):
        return self.length

    def __eq__(self, other):
        return list(self) == list(other)

    def __getitem__(self, index):
        for i, item in self.length:
            if i == index:
                return item

        raise IndexError

    def insert(self, value):
        self.head = Node(value, self.head)
        self.length += 1

    def append(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = node

        self.length += 1


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


