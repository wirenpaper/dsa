from libs.node import Node

class List:
    DEFAULT = "default"
    REVERSE = "reverse"

    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            self.head.push(data)

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
