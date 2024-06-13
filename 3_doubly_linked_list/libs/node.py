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

    def add_last(self, tail, data):
        tail.next = Node(data)
        prev = tail
        tail = tail.next
        tail.prev = prev
        return tail
