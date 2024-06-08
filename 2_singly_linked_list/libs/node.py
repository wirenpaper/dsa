class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def push(self, data):
        if self.next != None:
            self.next = self.next.push(data)
            return self
        self.next = Node(data)
        return self
