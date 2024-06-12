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
