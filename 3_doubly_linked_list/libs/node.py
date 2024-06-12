class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def add_first(self, data):
        cur = Node(data)
        cur.next = self
        self.prev = cur
        return cur
