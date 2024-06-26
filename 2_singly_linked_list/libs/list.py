from libs.node import Node

class List:
    # print modes
    DEFAULT = "default"
    REVERSE = "reverse"

    def __init__(self):
        self.head = None

    def add_first(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            self.head = self.head.add_first(data)

    def add_last(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            self.head.add_last(data)

    def remove_last(self):
        if self.head == None:
            return None
        elif self.head.next == None:
            _, res = self.head.remove_last()
            self.head = None
            return res
        else:
            _, res = self.head.remove_last()
            return res

    def remove_first(self):
        if self.head == None:
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            return data

    def print(self, mode="default"):
        if self.head != None:
            if mode == "default":
                self.head.print()
            elif mode == "reverse":
                self.head.rprint()
            else:
                print("invalid mode")
        else:
            print("empty list")
