from libs.node import Node

node = Node(3)
node = node.add_first(4)
print(node.data)
print(node.next.data)
print(node.next.prev.data)
