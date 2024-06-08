from libs.node import Node

class List:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head != Node:
            self.head = Node()
            self.head.data = data
        else:
            self.head.push(data)
