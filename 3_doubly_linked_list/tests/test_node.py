from libs.node import Node

def test_add_first():
    node = Node(3)

    node = node.add_first(4)
    assert node.data == 4
    assert node.next.data == 3
    assert node.next.prev.data == 4
    assert node.prev == None
    assert node.next.prev.prev == None

    node = node.add_first(5)
    assert node.data == 5
    assert node.next.data == 4
    assert node.next.prev.data == 5
    assert node.next.next.data == 3
    assert node.next.next.prev.data == 4
    assert node.prev == None
