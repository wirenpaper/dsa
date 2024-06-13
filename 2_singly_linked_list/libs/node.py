class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def add_first(self, data):
        cur = Node(data)
        cur.next = self
        return cur

    def add_last(self, data):
        if self.next != None:
            self.next = self.next.add_last(data)
            return self
        self.next = Node(data)
        return self

    def remove_last(self):
        if self.next != None:
            self.next, data = self.next.remove_last()
            return self, data
        return None, self.data

    def print(self):
        print(self.data)
        if self.next != None:
            self.next.print()

    def rprint(self):
        if self.next != None:
            self.next.rprint()
        print(self.data)
