class Node:
    def __init__(self):
        self.next = None

    def push(self, data):
        if self.next != None:
            self.next = self.next.push(data)
            return self
        cur = Node()
        cur.data = data
        self.next = cur
        return self
