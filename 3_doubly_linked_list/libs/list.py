from libs.node import Node

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.head = self.head.add_first(data)

    def add_last(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail = self.head.add_last(self.tail, data)

    def remove_last(self):
        if self.head == None:
            return None
        else:
            self.head, self.tail, data = self.head.remove_last()
            return data
