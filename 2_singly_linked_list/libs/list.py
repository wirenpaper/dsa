from libs.node import Node

class List:
    # print modes
    DEFAULT = "default"
    REVERSE = "reverse"

    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            self.head.push(data)

    def pop(self):
        if self.head == None:
            return None
        elif self.head.next == None:
            _, res = self.head.pop()
            self.head = None
            return res
        else:
            _, res = self.head.pop()
            return res

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
